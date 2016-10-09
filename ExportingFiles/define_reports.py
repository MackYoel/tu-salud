report_1 = {
    'model': 'Clientes',
    'rows': [
        ('CLIENTE id',                             'id'),
        ('CLIENTE chistoria',                      'chistoria'),
        # ('# rinosinusitis',                     'cantsinusitis'),
        # ('comentarios',                         'comentarios'),
        ('CLINICO id',                              'join(chistoria,Clinico.chistoria).id'),
        ('CLINICO tfecha',                          'join(chistoria,Clinico.chistoria).tfecha'),

    ]
}

# import re

# join_pattern = re.compile(r'^(join\((.*)\)\.)')
# for h, attr in report_1['rows']:
#     match = join_pattern.match(attr)
#     if match:
#         print('matched', attr)
#         print('match.group(1)', match.group(1))
#         print('match.group(2)', match.group(2), match.group(2).split(','))

