report_1 = {
    'model': 'Audiometria',
    'rows': [
        ('AUDIO id',                            'id'),
        ('AUDIO historia',                      'chistoria'),
        ('AUDIO fecha',                         'tfecha'),
        ('CLINICO tabaco',                      'join(chistoria,Clinico.chistoria).chabitostabaco'),
        ('CLINICO tfecha',                      'join(chistoria,Clinico.chistoria).tfecha'),
    ]
}
report_2 = {
    'model': 'Espirometria',
    'rows': [
        ('espi id',                            'id'),
        ('espi historia',                      'chistoria'),
        ('espi fecha',                         'tfecha'),
        ('CLINICO tabaco',                      'join(chistoria,Clinico.chistoria).chabitostabaco'),
        ('CLINICO tfecha',                      'join(chistoria,Clinico.chistoria).tfecha'),
    ]
}
report_3 = {
    'model': 'Espirometria',
    'rows': [
        ('espi id',                            'id'),
        ('espi historia',                      'chistoria'),
        ('espi fecha',                         'tfecha'),
        ('CLINICO tabaco',                      'join(chistoria,Clinico.chistoria).chabitostabaco'),
        ('CLINICO tfecha',                      'join(chistoria,Clinico.chistoria).tfecha'),
    ]
}

