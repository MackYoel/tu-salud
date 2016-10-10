report_1 = {
    'model': 'Audiometria',
    'rows': [
        ('AUDIO id',                            'id'),
        ('AUDIO historia',                      'chistoria'),
        ('AUDIO fecha',                         'tfecha'),
        ('CLINICO tabaco',                      'join(chistoria,Clinico.chistoria).chabitostabaco'),
    ]
}
