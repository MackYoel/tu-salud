import re
from . import models
from django.db.models import Q
from django.db.models.functions import Concat
from django.db.models import CharField
import datetime
import operator


JOIN_PATTERN = re.compile(r'^(join\((.*)\)\.)')


def generate_csv_serie():
    serie = [e for e in ALPHABET]
    serie.extend([l + _l for l in ALPHABET for _l in ALPHABET])
    return serie


def is_related_join(attr_string):
    return JOIN_PATTERN.match(attr_string)


def get_related_instance(instance, match, attr_string):
    self_attr, related_query = match.group(2).split(',')
    model_str, attr_str = related_query.split('.')

    filters = {
        attr_str: get_attribute(instance, self_attr),
        'tfecha__isnull': False
    }

    Model = getattr(models, model_str)
    try:
        _isntance = Model.objects.filter(**filters).latest('tfecha')
    except Model.DoesNotExist:
        return None
    else:
        return _isntance


def clear_attr_string(match, attr_string):
    return attr_string.replace(match.group(1), '')


def is_self_instance(attr_string):
    return attr_string == 'self'


def get_attribute(instance, attr_string):
    if is_self_instance(attr_string):
        return instance

    match = is_related_join(attr_string)
    if match:
        instance = get_related_instance(instance, match, attr_string)
        if not instance:
            return ''
        attr_string = clear_attr_string(match, attr_string)

    attrs = attr_string.split('.')
    value = instance
    for a in attrs:
        if not hasattr(value, a):
            return ''

        value = getattr(value, a)
    if isinstance(value, datetime.datetime):
        return str(value)
    return value


def get_q_filter_list(dict_filter):
    return [Q(**{df: dict_filter[df]}) for df in dict_filter]


def get_all_related_records(model, date_filter):
    _filter = get_q_filter_list(date_filter)
    return model.objects.annotate(chistoria_and_tfecha=Concat('chistoria', 'tfecha', output_field=CharField())).filter(*_filter)


def get_concatenated_rows(result):
    return [r.chistoria + str(r.tfecha)[:-9] for r in result]


def get_reduced_q_objects(date_filter, business):
    CD = models.ClientesDet
    date_filter['cempresa'] = business
    main_filters = get_q_filter_list(date_filter)
    result = CD.objects.filter(*main_filters)
    if result:
        rows = get_concatenated_rows(result)  # ['142729696002012-02-29']
        query = reduce(operator.or_, (Q(chistoria_and_tfecha__icontains=row) for row in rows))
        return query


ALPHABET = ''.join([chr(x) for x in range(65, 91)])
CSV_SERIE = generate_csv_serie()
