import re
from . import models


JOIN_PATTERN = re.compile(r'^(join\((.*)\)\.)')


def generate_csv_serie():
    serie = [e for e in ALPHABET]
    serie.extend([l + _l for l in ALPHABET for _l in ALPHABET])
    return serie


def is_related_join(attr_string):
    return JOIN_PATTERN.match(attr_string)
    # for h, attr in report_1['rows']:
    # if match:
    #     print('matched', attr)
    #     print('match.group(1)', match.group(1))
    #     print('match.group(2)', match.group(2), match.group(2).split(','))


def get_related_instance(instance, match, attr_string):
    self_attr, related_query = match.group(2).split(',')
    model_str, attr_str = related_query.split('.')

    filters = {
        attr_str: get_attribute(instance, self_attr),
        'tfecha__isnull': False
    }
    # import pdb
    # pdb.set_trace()

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
        # import pdb
        # pdb.set_trace()
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
    return str(value)


ALPHABET = ''.join([chr(x) for x in range(65, 91)])
CSV_SERIE = generate_csv_serie()
