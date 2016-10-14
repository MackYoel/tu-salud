# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.

from __future__ import unicode_literals

from django.db import models

from django.utils.translation import ugettext_lazy
from django.core.validators import MinValueValidator, MaxValueValidator


class Town(models.Model):
    name = models.CharField(max_length=50)
    county = models.CharField(max_length=50)

    class Meta:
        ordering = ['county', 'name']

    def __unicode__(self):
        return self.name


class Weather(models.Model):
    town = models.ForeignKey(
        Town,
        related_name=ugettext_lazy('town'))
    date = models.DateField()
    description = models.TextField()
    max_temperature = models.FloatField()
    min_temperature = models.FloatField()
    wind_speed = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name=ugettext_lazy('wind speed'))
    precipitation = models.IntegerField(
        verbose_name=ugettext_lazy('precipitation'))
    precipitation_probability = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name=ugettext_lazy('precipitation probability'))
    observations = models.TextField(
        verbose_name=ugettext_lazy('weather observations'))

    class Meta:
        verbose_name_plural = ugettext_lazy('weather')
        unique_together = (('town', 'date'))
        ordering = ['-date', 'town']

    def __unicode__(self):
        dtos = self.date.strftime('%d-%m-%Y')
        return self.town.name + " " + dtos


class ExportingfilesTown(models.Model):
    name = models.CharField(max_length=50)
    county = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ExportingFiles_town'


class ExportingfilesWeather(models.Model):
    date = models.DateField()
    description = models.TextField()
    max_temperature = models.FloatField()
    min_temperature = models.FloatField()
    wind_speed = models.IntegerField()
    precipitation = models.IntegerField()
    precipitation_probability = models.IntegerField()
    observations = models.TextField()
    town = models.ForeignKey(ExportingfilesTown)

    class Meta:
        managed = False
        db_table = 'ExportingFiles_weather'


class Absentismo(models.Model):
    chistoria = models.ForeignKey('Clientes', db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'absentismo'


class AbsentismoDet(models.Model):
    id = models.ForeignKey(Absentismo, db_column='id', blank=True, null=True)
    tfechaini = models.DateTimeField(blank=True, null=True)
    iddet = models.AutoField(primary_key=True)
    cenfermedad = models.CharField(max_length=100, blank=True, null=True)
    cdescripcion = models.CharField(max_length=100, blank=True, null=True)
    cyear = models.CharField(max_length=4, blank=True, null=True)
    casocisi = models.CharField(max_length=1, blank=True, null=True)
    casocino = models.CharField(max_length=1, blank=True, null=True)
    cdias = models.CharField(max_length=10, blank=True, null=True)
    item = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'absentismo_det'


class AbsentismoDetIud(models.Model):
    idop = models.CharField(max_length=1)
    idsimon = models.IntegerField(blank=True, null=True)
    iddetsimon = models.IntegerField(blank=True, null=True)
    item = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cenfermedad = models.CharField(max_length=100, blank=True, null=True)
    cdescripcion = models.CharField(max_length=100, blank=True, null=True)
    cyear = models.CharField(max_length=4, blank=True, null=True)
    cdias = models.CharField(max_length=10, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'absentismo_det_iud'


class AbsentismoIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'absentismo_iud'


class AccesoUsuario(models.Model):
    id_usuario = models.IntegerField(blank=True, null=True)
    id_form = models.IntegerField(blank=True, null=True)
    acceso = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    impresion = models.CharField(max_length=1, blank=True, null=True)
    eliminar = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acceso_usuario'


class Altura(models.Model):
    chistoria = models.ForeignKey('Clientes', db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    crecomendacion = models.CharField(max_length=200, blank=True, null=True)
    tec = models.CharField(max_length=1, blank=True, null=True)
    con = models.CharField(max_length=1, blank=True, null=True)
    mar = models.CharField(max_length=1, blank=True, null=True)
    aud = models.CharField(max_length=1, blank=True, null=True)
    equi = models.CharField(max_length=1, blank=True, null=True)
    sinco = models.CharField(max_length=1, blank=True, null=True)
    fobias = models.CharField(max_length=1, blank=True, null=True)
    psiqui = models.CharField(max_length=1, blank=True, null=True)
    cef = models.CharField(max_length=1, blank=True, null=True)
    cardio = models.CharField(max_length=1, blank=True, null=True)
    diabe = models.CharField(max_length=1, blank=True, null=True)
    vision = models.CharField(max_length=1, blank=True, null=True)
    respi = models.CharField(max_length=1, blank=True, null=True)
    hipoacu = models.CharField(max_length=1, blank=True, null=True)
    endo = models.CharField(max_length=1, blank=True, null=True)
    neuro = models.CharField(max_length=1, blank=True, null=True)
    conclus = models.CharField(max_length=200, blank=True, null=True)
    suste = models.CharField(max_length=1, blank=True, null=True)
    nigta = models.CharField(max_length=1, blank=True, null=True)
    nigtapro = models.CharField(max_length=1, blank=True, null=True)
    primeros = models.CharField(max_length=1, blank=True, null=True)
    entrena = models.CharField(max_length=1, blank=True, null=True)
    camlibre = models.CharField(max_length=1, blank=True, null=True)
    camlibre1 = models.CharField(max_length=1, blank=True, null=True)
    camlibre2 = models.CharField(max_length=1, blank=True, null=True)
    limita = models.CharField(max_length=1, blank=True, null=True)
    adiadodire = models.CharField(max_length=1, blank=True, null=True)
    adiadoindire = models.CharField(max_length=1, blank=True, null=True)
    rotar = models.CharField(max_length=1, blank=True, null=True)
    timpanos = models.CharField(max_length=1, blank=True, null=True)
    audicion = models.CharField(max_length=1, blank=True, null=True)
    cpieplano = models.CharField(max_length=1, blank=True, null=True)
    cplanos = models.CharField(max_length=1, blank=True, null=True)
    celectro = models.CharField(max_length=1, blank=True, null=True)
    tfechaaten = models.DateTimeField(blank=True, null=True)
    tfechavalido = models.DateTimeField(blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'altura'


class AlturaIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    crecomendacion = models.CharField(max_length=200, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'altura_iud'


class Anual(models.Model):
    chistoria = models.ForeignKey('Clientes', db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    crecomendaciones = models.CharField(max_length=500, blank=True, null=True)
    cdiagnostico = models.CharField(max_length=500, blank=True, null=True)
    cpuesto = models.CharField(max_length=30, blank=True, null=True)
    cpeso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ntalla = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    nindice = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    cimc = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    cbroca = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ccintura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ccadera = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    npresion = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    npresion2 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cespirometria = models.CharField(max_length=50, blank=True, null=True)
    caudiometriaderecho = models.CharField(max_length=100, blank=True, null=True)
    caudiometriaizquierdo = models.CharField(max_length=100, blank=True, null=True)
    caudiometriaderechodiag = models.CharField(max_length=20, blank=True, null=True)
    caudiometriaizquierdodiag = models.CharField(max_length=20, blank=True, null=True)
    cvisionderecho = models.CharField(max_length=40, blank=True, null=True)
    cvisionizquierdo = models.CharField(max_length=40, blank=True, null=True)
    costeomuscular = models.CharField(max_length=100, blank=True, null=True)
    crayos = models.CharField(max_length=40, blank=True, null=True)
    ccomentario = models.CharField(max_length=300, blank=True, null=True)
    cvisionderecho1 = models.CharField(max_length=6, blank=True, null=True)
    cvisionderecho2 = models.CharField(max_length=6, blank=True, null=True)
    cvisionizquierdo2 = models.CharField(max_length=6, blank=True, null=True)
    cvisionizquierdo1 = models.CharField(max_length=6, blank=True, null=True)
    cvisioni = models.CharField(max_length=40, blank=True, null=True)
    cvisiond = models.CharField(max_length=40, blank=True, null=True)
    claboratorio = models.CharField(max_length=150, blank=True, null=True)
    hemodiag = models.CharField(max_length=20, blank=True, null=True)
    orinadiag = models.CharField(max_length=20, blank=True, null=True)
    cvisionderech = models.CharField(max_length=40, blank=True, null=True)
    cvisionderech1 = models.CharField(max_length=40, blank=True, null=True)
    cvisionderech2 = models.CharField(max_length=40, blank=True, null=True)
    cvisionizquierd = models.CharField(max_length=40, blank=True, null=True)
    cvisionizquierd1 = models.CharField(max_length=40, blank=True, null=True)
    cvisionizquierd2 = models.CharField(max_length=40, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anual'


class AnualIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=500, blank=True, null=True)
    cdiagnostico = models.CharField(max_length=500, blank=True, null=True)
    cpuesto = models.CharField(max_length=30, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anual_iud'


class Apersona(models.Model):
    dni = models.BigIntegerField(blank=True, null=True)
    apellidos = models.CharField(max_length=25, blank=True, null=True)
    nombre = models.CharField(max_length=25, blank=True, null=True)
    passwd = models.CharField(max_length=25, blank=True, null=True)
    login = models.CharField(max_length=25, blank=True, null=True)
    idpersona = models.BigIntegerField(primary_key=True)
    sucursal = models.CharField(max_length=100, blank=True, null=True)
    flg_activo = models.NullBooleanField()
    flg_auth = models.NullBooleanField()
    flg_confir = models.NullBooleanField()
    idpuesto = models.ForeignKey('Asitpuestos', db_column='idpuesto', blank=True, null=True)
    huella = models.BinaryField(blank=True, null=True)
    fech_reg = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apersona'


class Ascenso(models.Model):
    chistoria = models.ForeignKey('Clientes', db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    canemia = models.CharField(max_length=1, blank=True, null=True)
    ccirugia = models.CharField(max_length=1, blank=True, null=True)
    cdesor = models.CharField(max_length=1, blank=True, null=True)
    cdiabe = models.CharField(max_length=1, blank=True, null=True)
    chiper = models.CharField(max_length=1, blank=True, null=True)
    cemba = models.CharField(max_length=1, blank=True, null=True)
    cprobne = models.CharField(max_length=1, blank=True, null=True)
    cinfneu = models.CharField(max_length=1, blank=True, null=True)
    cinfrec = models.CharField(max_length=1, blank=True, null=True)
    cobesidad = models.CharField(max_length=1, blank=True, null=True)
    cprobcar = models.CharField(max_length=1, blank=True, null=True)
    cprobres = models.CharField(max_length=1, blank=True, null=True)
    cproboft = models.CharField(max_length=1, blank=True, null=True)
    capnea = models.CharField(max_length=1, blank=True, null=True)
    cotras = models.CharField(max_length=1, blank=True, null=True)
    calerg = models.CharField(max_length=1, blank=True, null=True)
    cuso = models.CharField(max_length=1, blank=True, null=True)
    cpor = models.CharField(max_length=1, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    capto = models.CharField(max_length=1, blank=True, null=True)
    cobservacion = models.TextField(blank=True, null=True)
    cpor2 = models.CharField(max_length=1, blank=True, null=True)
    cpor1 = models.CharField(max_length=1, blank=True, null=True)
    cnoapto = models.CharField(max_length=1, blank=True, null=True)
    cflag = models.CharField(max_length=1, blank=True, null=True)
    cedema = models.CharField(max_length=1, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    medactu = models.CharField(max_length=200, blank=True, null=True)
    electro = models.CharField(max_length=200, blank=True, null=True)
    esfuerzo = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ascenso'


class AscensoIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cobservacion = models.TextField(blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ascenso_iud'


class AsistFeriado(models.Model):
    idsucursal = models.ForeignKey('AsistSucursal', db_column='idsucursal', blank=True, null=True)
    fech_feriado = models.DateTimeField(blank=True, null=True)
    flg_sucursal = models.CharField(max_length=25, blank=True, null=True)
    desferiado = models.CharField(max_length=50, blank=True, null=True)
    idferiado = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'asist_feriado'


class AsistHuella(models.Model):
    idhuella = models.BigIntegerField()
    idper = models.BigIntegerField(blank=True, null=True)
    huella = models.BinaryField(blank=True, null=True)
    fechreg = models.DateTimeField(blank=True, null=True)
    numhuella = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asist_huella'


class AsistSucursal(models.Model):
    idsucursal = models.BigIntegerField(primary_key=True)
    dessucursal = models.CharField(max_length=25, blank=True, null=True)
    flg_activo = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'asist_sucursal'


class Asistareas(models.Model):
    idarea = models.BigIntegerField(primary_key=True)
    desarea = models.CharField(max_length=50, blank=True, null=True)
    fechreg = models.DateTimeField(blank=True, null=True)
    idsuc = models.BigIntegerField(blank=True, null=True)
    flg_activo = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'asistareas'


class AsistcontCab(models.Model):
    fechregistro = models.DateTimeField(blank=True, null=True)
    codasist = models.BigIntegerField(primary_key=True)
    idsuc = models.BigIntegerField(blank=True, null=True)
    idhorario = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asistcont_cab'


class AsistcontDeta(models.Model):
    codasistcab = models.ForeignKey(AsistcontCab, db_column='codasistcab', blank=True, null=True)
    horat = models.DateTimeField(blank=True, null=True)
    fechreg = models.DateTimeField(blank=True, null=True)
    horatipo = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asistcont_deta'


class Asisthorario(models.Model):
    horaingr = models.DateTimeField(blank=True, null=True)
    horasali = models.DateTimeField(blank=True, null=True)
    idper = models.BigIntegerField(blank=True, null=True)
    fechreg = models.DateTimeField(blank=True, null=True)
    flgactivo = models.NullBooleanField()
    idhorario = models.BigIntegerField(primary_key=True)
    flagbreak = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'asisthorario'


class AsisthorarioDet(models.Model):
    idhordet = models.ForeignKey(Asisthorario, db_column='idhordet', blank=True, null=True)
    ndia = models.BigIntegerField(blank=True, null=True)
    idndia = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'asisthorario_det'


class Asistpermiso(models.Model):
    estado = models.CharField(max_length=50, blank=True, null=True)
    horip = models.DateTimeField(blank=True, null=True)
    horfp = models.DateTimeField(blank=True, null=True)
    idpersona = models.BigIntegerField(blank=True, null=True)
    idpermiso = models.BigIntegerField(primary_key=True)
    fechreg = models.DateTimeField(blank=True, null=True)
    motivoper = models.CharField(max_length=500, blank=True, null=True)
    id_auth = models.BigIntegerField(blank=True, null=True)
    id_conf = models.BigIntegerField(blank=True, null=True)
    flg_activo = models.NullBooleanField()
    estado_confir = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asistpermiso'


class Asithuella(models.Model):
    idper = models.BigIntegerField()
    despuesto = models.CharField(max_length=50, blank=True, null=True)
    fech_reg = models.DateTimeField(blank=True, null=True)
    huella = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asithuella'


class Asitpuestos(models.Model):
    idpuestos = models.BigIntegerField(primary_key=True)
    idarepuest = models.ForeignKey(Asistareas, db_column='idarepuest', blank=True, null=True)
    despuesto = models.CharField(max_length=50, blank=True, null=True)
    fechreg = models.DateTimeField(blank=True, null=True)
    flg_activo = models.NullBooleanField()
    idjefe = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asitpuestos'


class Audiometria(models.Model):
    # chistoria = models.ForeignKey('Clientes', db_column='chistoria', blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    caudio = models.CharField(max_length=1, blank=True, null=True)
    cantrinitis = models.CharField(max_length=1, blank=True, null=True)
    cantsinusitis = models.CharField(max_length=1, blank=True, null=True)
    cantmeningitis = models.CharField(max_length=1, blank=True, null=True)
    cantparotiditis = models.CharField(max_length=1, blank=True, null=True)
    cantsarampion = models.CharField(max_length=1, blank=True, null=True)
    cantsordera = models.CharField(max_length=1, blank=True, null=True)
    cantotitismedia = models.CharField(max_length=1, blank=True, null=True)
    cantpracticatiro = models.CharField(max_length=1, blank=True, null=True)
    cantanttimpa = models.CharField(max_length=1, blank=True, null=True)
    csinacuferos = models.CharField(max_length=1, blank=True, null=True)
    csinvertigo = models.CharField(max_length=1, blank=True, null=True)
    csinmareos = models.CharField(max_length=1, blank=True, null=True)
    csinotalgias = models.CharField(max_length=1, blank=True, null=True)
    csinseotalgias = models.CharField(max_length=1, blank=True, null=True)
    csinserdera = models.CharField(max_length=1, blank=True, null=True)
    csinobservacion = models.TextField(blank=True, null=True)
    cdesruido = models.TextField(blank=True, null=True)
    cporepp = models.CharField(max_length=12, blank=True, null=True)
    ctiemepp = models.CharField(max_length=10, blank=True, null=True)
    cusotapo = models.CharField(max_length=1, blank=True, null=True)
    cusoore = models.CharField(max_length=1, blank=True, null=True)
    cusomix = models.CharField(max_length=1, blank=True, null=True)
    cusootro = models.CharField(max_length=1, blank=True, null=True)
    cevaotood = models.CharField(max_length=1, blank=True, null=True)
    cevaotooi = models.CharField(max_length=1, blank=True, null=True)
    cdiagnoklock = models.TextField(blank=True, null=True)
    cdiagnomodi = models.TextField(blank=True, null=True)
    chandicap = models.TextField(blank=True, null=True)
    cfreva125od = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva125oi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva250od = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva250oi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva500od = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva500oi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva1000od = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva1000oi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva2000od = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva2000oi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva3000od = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva3000oi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva4000od = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva4000oi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva6000od = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva6000oi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva8000od = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfreva8000oi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfrevo125od = models.CharField(max_length=4, blank=True, null=True)
    cfrevo125oi = models.CharField(max_length=3, blank=True, null=True)
    cfrevo250od = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfrevo250oi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfrevo500od = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfrevo500oi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfrevo1000od = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfrevo1000oi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfrevo2000od = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfrevo2000oi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfrevo3000od = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfrevo3000oi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfrevo4000od = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfrevo4000oi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfrevo6000od = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfrevo6000oi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cfrevo8000od = models.CharField(max_length=3, blank=True, null=True)
    cfrevo8000oi = models.CharField(max_length=3, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    cdiagnosticos = models.CharField(max_length=100, blank=True, null=True)
    year = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    cdiagnosticosod = models.CharField(max_length=100, blank=True, null=True)
    cdiagnosticosoi = models.CharField(max_length=100, blank=True, null=True)
    ccie10 = models.CharField(max_length=8, blank=True, null=True)
    ctabaco = models.CharField(max_length=1, blank=True, null=True)
    cquimicos = models.CharField(max_length=1, blank=True, null=True)
    chobbies = models.CharField(max_length=1, blank=True, null=True)
    ctoxicos = models.CharField(max_length=1, blank=True, null=True)
    cinfecciones = models.CharField(max_length=1, blank=True, null=True)
    cdolor = models.CharField(max_length=1, blank=True, null=True)
    cdisminucion = models.CharField(max_length=1, blank=True, null=True)
    cmareos = models.CharField(max_length=1, blank=True, null=True)
    czumbidos = models.CharField(max_length=1, blank=True, null=True)
    cservicio = models.CharField(max_length=1, blank=True, null=True)
    cevaotooddes = models.CharField(max_length=100, blank=True, null=True)
    cevaotooides = models.CharField(max_length=100, blank=True, null=True)
    cexposi = models.CharField(max_length=1, blank=True, null=True)
    ctrianguloder = models.CharField(max_length=8, blank=True, null=True)
    ctrianguloizq = models.CharField(max_length=8, blank=True, null=True)
    cperforader = models.CharField(max_length=8, blank=True, null=True)
    cperforaizq = models.CharField(max_length=8, blank=True, null=True)
    cabombader = models.CharField(max_length=8, blank=True, null=True)
    cabombaizq = models.CharField(max_length=8, blank=True, null=True)
    ccerumender = models.CharField(max_length=8, blank=True, null=True)
    ccerumenizq = models.CharField(max_length=8, blank=True, null=True)
    caudicionder = models.CharField(max_length=1, blank=True, null=True)
    caudicionizq = models.CharField(max_length=1, blank=True, null=True)
    caudioaereaod = models.CharField(max_length=1, blank=True, null=True)
    caudioaereaoi = models.CharField(max_length=1, blank=True, null=True)
    caudiooseaod = models.CharField(max_length=1, blank=True, null=True)
    caudiooseaoi = models.CharField(max_length=1, blank=True, null=True)
    ccerrado = models.CharField(max_length=1, blank=True, null=True)
    idcalibracion = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audiometria'


class AudiometriaIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnoklock = models.TextField(blank=True, null=True)
    cdiagnomodi = models.TextField(blank=True, null=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    cdiagnosticos = models.CharField(max_length=100, blank=True, null=True)
    cdiagnosticosod = models.CharField(max_length=100, blank=True, null=True)
    cdiagnosticosoi = models.CharField(max_length=100, blank=True, null=True)
    ccerrado = models.CharField(max_length=1, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audiometria_iud'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
          


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
          


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
          


class Autori(models.Model):
    chistoria = models.ForeignKey('Clientes', db_column='chistoria', blank=True, null=True)
    datos_anterior = models.TextField(blank=True, null=True)
    datos_nuevo = models.TextField(blank=True, null=True)
    idpersonal = models.CharField(max_length=5, blank=True, null=True)
    idpersonal_autoriza = models.CharField(max_length=4, blank=True, null=True)
    estado = models.CharField(max_length=3, blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    fecha_anterior = models.DateTimeField(blank=True, null=True)
    examen = models.CharField(max_length=2, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autori'


class Bitacora(models.Model):
    id_usuario = models.IntegerField(blank=True, null=True)
    id_form = models.IntegerField(blank=True, null=True)
    descrip = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitacora'


class C(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    idop = models.CharField(max_length=1, blank=True, null=True)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cnombre = models.CharField(max_length=100, blank=True, null=True)
    capellidos = models.CharField(max_length=100, blank=True, null=True)
    cdni = models.CharField(max_length=8, blank=True, null=True)
    dfecnac = models.DateField(blank=True, null=True)
    cpuesto = models.CharField(max_length=255, blank=True, null=True)
    ccampo = models.CharField(max_length=30, blank=True, null=True)
    cempresa = models.CharField(max_length=11, blank=True, null=True)
    ctelefono = models.CharField(max_length=9, blank=True, null=True)
    ccelular = models.CharField(max_length=9, blank=True, null=True)
    ccelular2 = models.CharField(max_length=9, blank=True, null=True)
    cperfiles = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_'


class CFormulario(models.Model):
    id_form = models.IntegerField(blank=True, null=True)
    formulario = models.CharField(max_length=100, blank=True, null=True)
    descrip = models.TextField(blank=True, null=True)
    accede_de = models.TextField(blank=True, null=True)
    habilitado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    existe = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nuevo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_formulario'


class CGrupo(models.Model):
    id_grupo = models.IntegerField(blank=True, null=True)
    grupo = models.CharField(max_length=50, blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    habilitado = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_grupo'


class CUnidad(models.Model):
    id_unidad = models.IntegerField(blank=True, null=True)
    unidad = models.CharField(max_length=40, blank=True, null=True)
    orden = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    desripcion = models.TextField(blank=True, null=True)
    habilitado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_unidad'


class Cabcargo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    tfecha = models.DateField(blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cabcargo'


class Cabespecia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    servicio = models.CharField(max_length=2, blank=True, null=True)
    periodo = models.DateField(blank=True, null=True)
    sucursal = models.CharField(max_length=2, blank=True, null=True)
    tfecha = models.DateField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cabespecia'


class Cabexpediente(models.Model):
    chistoria = models.ForeignKey('Clientes', db_column='chistoria')
    cestado = models.CharField(max_length=20, blank=True, null=True)
    dregistro = models.DateField(blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cabexpediente'


class Calibracion(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    serie = models.CharField(max_length=50, blank=True, null=True)
    fechacal = models.DateField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    usuario = models.CharField(max_length=5, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    cespeci = models.CharField(max_length=3, blank=True, null=True)
    equipo = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calibracion'


class Cardiograma(models.Model):
    chistoria = models.ForeignKey('Clientes', db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    critmo = models.CharField(max_length=20, blank=True, null=True)
    cfrecuencia = models.CharField(max_length=3, blank=True, null=True)
    ceje = models.CharField(max_length=3, blank=True, null=True)
    condap = models.CharField(max_length=3, blank=True, null=True)
    cqrs = models.CharField(max_length=3, blank=True, null=True)
    cpr = models.CharField(max_length=3, blank=True, null=True)
    cqt = models.CharField(max_length=3, blank=True, null=True)
    cdiagnostico = models.CharField(max_length=200, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    cpruebaes = models.TextField(blank=True, null=True)
    ccie10 = models.CharField(max_length=8, blank=True, null=True)
    challasgos = models.CharField(max_length=80, blank=True, null=True)
    clectura = models.CharField(max_length=2, blank=True, null=True)
    idcalibracion = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cardiograma'


class CardiogramaIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.CharField(max_length=200, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    challasgos = models.CharField(max_length=80, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cardiograma_iud'


class Cargos(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=25)
    area = models.CharField(max_length=10)
    csucursal = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargos'


class Cie10(models.Model):
    id = models.CharField(max_length=4, primary_key=True)
    cdescie10 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cie10'


class Cierre(models.Model):
    chistoria = models.ForeignKey('Clientes', db_column='chistoria', blank=True, null=True)
    tfecha = models.DateField(blank=True, null=True)
    tfecha2 = models.DateTimeField(blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    cperfil = models.CharField(max_length=50, blank=True, null=True)
    ccantidad = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cempresa = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cierre'


class Citascab(models.Model):
    tfecha = models.DateTimeField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    ncupo = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    cturno = models.CharField(max_length=10, blank=True, null=True)
    dfecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citascab'


class Citasdet(models.Model):
    tfecha = models.DateTimeField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    idcitas = models.IntegerField(blank=True, null=True)
    chistoria = models.ForeignKey('Clientes', db_column='chistoria', blank=True, null=True)
    cturno = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citasdet'


class Citaswebcab(models.Model):
    nrocita = models.IntegerField(blank=True, null=True)
    cuserlogin = models.CharField(max_length=10, blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    cruc = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citaswebcab'


class Citaswebdet(models.Model):
    cdni = models.CharField(max_length=8, blank=True, null=True)
    cturno = models.CharField(max_length=10, blank=True, null=True)
    cuserlogin = models.CharField(max_length=10, blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    capellidos = models.CharField(max_length=100, blank=True, null=True)
    cnombre = models.CharField(max_length=100, blank=True, null=True)
    nrocita = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citaswebdet'


class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    chistoria = models.CharField(primary_key=True, max_length=11)
    capellidos = models.CharField(max_length=100, blank=True, null=True)
    cnombre = models.CharField(max_length=100, blank=True, null=True)
    cestciv = models.CharField(max_length=5, blank=True, null=True)
    csexo = models.CharField(max_length=5, blank=True, null=True)
    cgrado = models.CharField(max_length=5, blank=True, null=True)
    cdomicilio = models.CharField(max_length=200, blank=True, null=True)
    cubigeo = models.CharField(max_length=6, blank=True, null=True)
    dfecnac = models.DateField(blank=True, null=True)
    ctelefono = models.CharField(max_length=9, blank=True, null=True)
    ccelular = models.CharField(max_length=9, blank=True, null=True)
    ccelular2 = models.CharField(max_length=9, blank=True, null=True)
    cpuesto = models.CharField(max_length=255, blank=True, null=True)
    cempresa = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    # id = models.AutoField(primary_key=True)
    ctipdoc = models.CharField(max_length=1, blank=True, null=True)
    cdni = models.CharField(max_length=8, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    cperfiles = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    csanidad = models.CharField(max_length=1, blank=True, null=True)
    ccorreo = models.CharField(max_length=50, blank=True, null=True)
    clugar = models.CharField(max_length=50, blank=True, null=True)
    cdomicilio2 = models.CharField(max_length=90)
    creslug = models.CharField(max_length=8, blank=True, null=True)
    ctielug = models.CharField(max_length=2, blank=True, null=True)
    csegurodes = models.CharField(max_length=50, blank=True, null=True)
    cprofesion = models.CharField(max_length=50, blank=True, null=True)
    cseguro = models.CharField(max_length=3, blank=True, null=True)
    cminas = models.CharField(max_length=30, blank=True, null=True)
    cedad = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ccontrata = models.CharField(max_length=11, blank=True, null=True)
    centregado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tfecha2 = models.DateTimeField(blank=True, null=True)
    ccampo = models.CharField(max_length=30, blank=True, null=True)
    cagencia = models.CharField(max_length=20, blank=True, null=True)
    ncorrelativo = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    cempresa1 = models.CharField(max_length=100, blank=True, null=True)
    texamen = models.CharField(max_length=100, blank=True, null=True)
    ntrabajo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class ClientesDet(models.Model):
    # cliente = 
    chistoria = models.CharField(max_length=11)
    cpuesto = models.CharField(max_length=255, blank=True, null=True)
    cempresa = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'clientes_det'


class ClientesIud(models.Model):
    idop = models.CharField(max_length=1, blank=True, null=True)
    idchistoria = models.CharField(max_length=16)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11)
    cnombre = models.CharField(max_length=100, blank=True, null=True)
    capellidos = models.CharField(max_length=100, blank=True, null=True)
    cdni = models.CharField(max_length=8, blank=True, null=True)
    dfecnac = models.DateField(blank=True, null=True)
    cpuesto = models.CharField(max_length=255, blank=True, null=True)
    ccampo = models.CharField(max_length=30, blank=True, null=True)
    cempresa = models.CharField(max_length=11, blank=True, null=True)
    ctelefono = models.CharField(max_length=9, blank=True, null=True)
    ccelular = models.CharField(max_length=9, blank=True, null=True)
    ccelular2 = models.CharField(max_length=9, blank=True, null=True)
    cperfiles = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes_iud'


class Clinico(models.Model):
    # chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    chistoria = models.CharField(primary_key=True, max_length=11)
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    cantedm = models.CharField(max_length=1, blank=True, null=True)
    cantehta = models.CharField(max_length=1, blank=True, null=True)
    canteasma = models.CharField(max_length=1, blank=True, null=True)
    cantehipertrig = models.CharField(max_length=1, blank=True, null=True)
    cantehipercoles = models.CharField(max_length=1, blank=True, null=True)
    cantecardiov = models.CharField(max_length=1, blank=True, null=True)
    cantealergias = models.CharField(max_length=1, blank=True, null=True)
    canteartropa = models.CharField(max_length=1, blank=True, null=True)
    cantecolumna = models.CharField(max_length=1, blank=True, null=True)
    cantehbp = models.CharField(max_length=1, blank=True, null=True)
    cantemigra = models.CharField(max_length=1, blank=True, null=True)
    canteqx = models.CharField(max_length=1, blank=True, null=True)
    canteotras = models.CharField(max_length=200, blank=True, null=True)
    cantefamili = models.CharField(max_length=100, blank=True, null=True)
    cantefamip = models.CharField(max_length=250, blank=True, null=True)
    cantefamim = models.CharField(max_length=250, blank=True, null=True)
    cantefamiher = models.CharField(max_length=100, blank=True, null=True)
    cnumerosinhijos = models.CharField(max_length=1, blank=True, null=True)
    cnumerohijosvivos = models.IntegerField(blank=True, null=True)
    cnumerohijosmuertos = models.IntegerField(blank=True, null=True)
    chabitostabaco = models.CharField(max_length=3, blank=True, null=True)
    chabitosalcohol = models.CharField(max_length=3, blank=True, null=True)
    chabitosdrogas = models.CharField(max_length=3, blank=True, null=True)
    cdifperso = models.CharField(max_length=12, blank=True, null=True)
    ccintura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ccadera = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    ctipoempresa = models.CharField(max_length=3, blank=True, null=True)
    csupetrab = models.CharField(max_length=1, blank=True, null=True)
    cconctrab = models.CharField(max_length=1, blank=True, null=True)
    csubstrab = models.CharField(max_length=1, blank=True, null=True)
    caltura = models.CharField(max_length=3, blank=True, null=True)
    cagenteruido = models.CharField(max_length=1, blank=True, null=True)
    cpuesto = models.CharField(max_length=80, blank=True, null=True)
    cpuesactu = models.CharField(max_length=80, blank=True, null=True)
    ctiempo = models.CharField(max_length=20, blank=True, null=True)
    creubicacion = models.CharField(max_length=1, blank=True, null=True)
    cagentepolvo = models.CharField(max_length=1, blank=True, null=True)
    cagentevibse = models.CharField(max_length=1, blank=True, null=True)
    cagentevibto = models.CharField(max_length=1, blank=True, null=True)
    cagentecance = models.CharField(max_length=1, blank=True, null=True)
    cagentemuta = models.CharField(max_length=1, blank=True, null=True)
    cagentesolve = models.CharField(max_length=1, blank=True, null=True)
    cagentemetal = models.CharField(max_length=1, blank=True, null=True)
    cagentetempe = models.CharField(max_length=1, blank=True, null=True)
    cagentebiolo = models.CharField(max_length=1, blank=True, null=True)
    cagentepost = models.CharField(max_length=1, blank=True, null=True)
    cagenteturno = models.CharField(max_length=1, blank=True, null=True)
    cagentecargas = models.CharField(max_length=1, blank=True, null=True)
    cagentemovrep = models.CharField(max_length=1, blank=True, null=True)
    cagenteotros = models.CharField(max_length=1, blank=True, null=True)
    nindice = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    nsupcor = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    cimc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cbroca = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cporgrasa = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    diagnostico = models.CharField(max_length=100, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    calergia = models.CharField(max_length=40, blank=True, null=True)
    cinmuni = models.CharField(max_length=120, blank=True, null=True)
    ccie10 = models.CharField(max_length=20, blank=True, null=True)
    cniega = models.CharField(max_length=1, blank=True, null=True)
    cfur = models.CharField(max_length=5, blank=True, null=True)
    crcirre = models.CharField(max_length=1, blank=True, null=True)
    crcregu = models.CharField(max_length=1, blank=True, null=True)
    crcdias = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    crctiem = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    cirs = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    cmac = models.CharField(max_length=1, blank=True, null=True)
    cinicio = models.CharField(max_length=1, blank=True, null=True)
    ctermino = models.CharField(max_length=1, blank=True, null=True)
    cpuestoope = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinico'


class ClinicoIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    diagnostico = models.CharField(max_length=100, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinico_iud'


class Conf(models.Model):
    idconf = models.AutoField(primary_key=True)
    server = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conf'


class Contrata(models.Model):
    cnombre = models.CharField(max_length=50)
    tfecha = models.DateTimeField(blank=True, null=True)
    cnota = models.TextField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    cruc = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contrata'


class Controlcitastmp(models.Model):
    nrocita = models.AutoField(primary_key=True)
    cdni = models.CharField(max_length=8, blank=True, null=True)
    capellidos = models.CharField(max_length=100, blank=True, null=True)
    cnombre = models.CharField(max_length=100, blank=True, null=True)
    cpuesto = models.CharField(max_length=200, blank=True, null=True)
    cperfil = models.CharField(max_length=100, blank=True, null=True)
    cempresa = models.CharField(max_length=200, blank=True, null=True)
    ccontratista = models.CharField(max_length=200, blank=True, null=True)
    dfechacita = models.DateTimeField(blank=True, null=True)
    dfechareg = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'controlcitastmp'


class Controldatos(models.Model):
    chistoria = models.CharField(primary_key=True, max_length=11)
    tfecha = models.DateTimeField(blank=True, null=True)
    bestado = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'controldatos'


class Controldatosdet(models.Model):
    chistoria = models.ForeignKey(Controldatos, db_column='chistoria', blank=True, null=True)
    cestado = models.CharField(max_length=15, blank=True, null=True)
    tfechacheck = models.DateTimeField(blank=True, null=True)
    cconsultorio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'controldatosdet'


class Controlexp(models.Model):
    idinforme = models.BigIntegerField()
    ninforme = models.CharField(max_length=25, blank=True, null=True)
    ruta = models.CharField(max_length=200, blank=True, null=True)
    grupoemp = models.CharField(max_length=25, blank=True, null=True)
    fila = models.BigIntegerField(blank=True, null=True)
    col = models.BigIntegerField(blank=True, null=True)
    campo = models.CharField(max_length=200, blank=True, null=True)
    tabla = models.CharField(max_length=200, blank=True, null=True)
    fech_reg = models.DateTimeField(blank=True, null=True)
    orden = models.BigIntegerField(blank=True, null=True)
    compuesto = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'controlexp'


class Conversion(models.Model):
    cescala = models.CharField(max_length=3, blank=True, null=True)
    cmm = models.CharField(max_length=2, blank=True, null=True)
    cvalor = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    csexo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conversion'


class Dermatologico(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    cenfermedadcual = models.TextField(blank=True, null=True)
    cenfermedad = models.CharField(max_length=1, blank=True, null=True)
    calergiacual = models.TextField(blank=True, null=True)
    calergia = models.CharField(max_length=1, blank=True, null=True)
    cmedicacion = models.TextField(blank=True, null=True)
    ccara = models.CharField(max_length=1, blank=True, null=True)
    cpecho = models.CharField(max_length=1, blank=True, null=True)
    cespalda = models.CharField(max_length=1, blank=True, null=True)
    cbrazos = models.CharField(max_length=1, blank=True, null=True)
    cpiernas = models.CharField(max_length=1, blank=True, null=True)
    ccabello = models.CharField(max_length=1, blank=True, null=True)
    cenrojecido = models.CharField(max_length=1, blank=True, null=True)
    ccuando = models.TextField(blank=True, null=True)
    cdonde = models.TextField(blank=True, null=True)
    culcera = models.CharField(max_length=1, blank=True, null=True)
    ccuando1 = models.TextField(blank=True, null=True)
    cdonde1 = models.TextField(blank=True, null=True)
    cresequedad = models.CharField(max_length=1, blank=True, null=True)
    ccuando2 = models.TextField(blank=True, null=True)
    cdonde2 = models.TextField(blank=True, null=True)
    cronchas = models.CharField(max_length=1, blank=True, null=True)
    cdesca = models.CharField(max_length=1, blank=True, null=True)
    cespeci = models.TextField(blank=True, null=True)
    cespeci2 = models.TextField(blank=True, null=True)
    cengrosa = models.CharField(max_length=1, blank=True, null=True)
    ccuando3 = models.TextField(blank=True, null=True)
    cdiagnostico = models.CharField(max_length=100, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    ccie10 = models.CharField(max_length=20, blank=True, null=True)
    cmedica = models.CharField(max_length=1, blank=True, null=True)
    ccabello2 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dermatologico'


class DermatologicoIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dermatologico_iud'


class Detcargo(models.Model):
    id = models.AutoField(primary_key=True)
    idperfil = models.IntegerField(blank=True, null=True)
    idcargo = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    tfecha = models.DateField(blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    idcab = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detcargo'


class Detespecia(models.Model):
    id = models.AutoField(primary_key=True)
    idcab = models.IntegerField(blank=True, null=True)
    tfecha = models.DateField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cempresa = models.CharField(max_length=11, blank=True, null=True)
    costo = models.IntegerField(blank=True, null=True)
    autorizacion = models.CharField(max_length=100, blank=True, null=True)
    obser = models.CharField(max_length=100, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detespecia'


class Detexpediente(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    cestado = models.CharField(max_length=20, blank=True, null=True)
    bcontrol = models.NullBooleanField()
    dfec_reg = models.DateField(blank=True, null=True)
    norden = models.IntegerField(blank=True, null=True)
    cdocumento = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detexpediente'


class Disttab(models.Model):
    ccodtab = models.CharField(max_length=3, blank=True, null=True)
    ccodigo = models.CharField(max_length=2, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    crecomendacion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disttab'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
          


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Docdetcargo(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    idcargo = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    usuari = models.CharField(max_length=5, blank=True, null=True)
    tfecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'docdetcargo'


class Ecografia(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    ctipexa = models.CharField(max_length=3, blank=True, null=True)
    cinforme = models.TextField(blank=True, null=True)
    cconclusion = models.TextField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ecografia'


class EcografiaIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    ctipexa = models.CharField(max_length=3, blank=True, null=True)
    cinforme = models.TextField(blank=True, null=True)
    cconclusion = models.TextField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecografia_iud'


class Empresa(models.Model):
    cnombre = models.CharField(max_length=100)
    ccodruc = models.CharField(max_length=11)
    crubro = models.CharField(max_length=50, blank=True, null=True)
    cdomicilio = models.TextField(blank=True, null=True)
    ctelefono = models.CharField(max_length=9, blank=True, null=True)
    ccontacto = models.CharField(max_length=100, blank=True, null=True)
    cemail = models.TextField(blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    ngrupo = models.ForeignKey('Grupo', db_column='ngrupo', blank=True, null=True)
    ctipoem = models.CharField(max_length=3, blank=True, null=True)
    cnota = models.TextField(blank=True, null=True)
    cfax = models.CharField(max_length=9, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    cactivi = models.CharField(max_length=40, blank=True, null=True)
    cactividad = models.CharField(max_length=1, blank=True, null=True)
    cciudad = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class EmpresaCliente(models.Model):
    ccodruc = models.CharField(max_length=11, blank=True, null=True)
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateField(blank=True, null=True)
    cestnuevo = models.CharField(max_length=1, blank=True, null=True)
    ctipohist = models.CharField(max_length=3, blank=True, null=True)
    tfechaexamen = models.DateField(blank=True, null=True)
    ctipoempresa = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa_cliente'


class EmpresaIud(models.Model):
    idop = models.CharField(max_length=1, blank=True, null=True)
    idccodruc = models.CharField(max_length=16)
    idsimon = models.IntegerField(blank=True, null=True)
    ccodruc = models.CharField(max_length=11)
    cnombre = models.CharField(max_length=100)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa_iud'


class Enroll(models.Model):
    id = models.AutoField(primary_key=True)
    ssn = models.CharField(max_length=50, blank=True, null=True)
    template = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enroll'


class Entregacargo(models.Model):
    cnombre = models.CharField(max_length=50)
    tfecha = models.DateTimeField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    texto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entregacargo'


class Espirometria(models.Model):
    #chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    cfuncrespiabs = models.CharField(max_length=7, blank=True, null=True)
    cfvc = models.CharField(max_length=7, blank=True, null=True)
    cfef1 = models.CharField(max_length=7, blank=True, null=True)
    cfev_fvc = models.CharField(max_length=7, blank=True, null=True)
    cfef_23_75 = models.CharField(max_length=7, blank=True, null=True)
    cinterpretacion = models.CharField(max_length=100, blank=True, null=True)
    cinforme = models.TextField(blank=True, null=True)
    cmmv = models.CharField(max_length=7, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cfumador = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    cdiagnosticos = models.CharField(max_length=100, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    ccie10 = models.CharField(max_length=4, blank=True, null=True)
    cfvcpor = models.CharField(max_length=7, blank=True, null=True)
    cfef1por = models.CharField(max_length=7, blank=True, null=True)
    cfev_fvcpor = models.CharField(max_length=7, blank=True, null=True)
    cfef_23_75por = models.CharField(max_length=7, blank=True, null=True)
    idcalibracion = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'espirometria'


class EspirometriaIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cinterpretacion = models.CharField(max_length=100, blank=True, null=True)
    cinforme = models.TextField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnosticos = models.CharField(max_length=100, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'espirometria_iud'


class Estruc(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    crecomendacion = models.CharField(max_length=200, blank=True, null=True)
    apto = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    noapto = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    tec = models.CharField(max_length=1, blank=True, null=True)
    ver = models.CharField(max_length=1, blank=True, null=True)
    mio = models.CharField(max_length=1, blank=True, null=True)
    mig = models.CharField(max_length=1, blank=True, null=True)
    lab = models.CharField(max_length=1, blank=True, null=True)
    arrit = models.CharField(max_length=1, blank=True, null=True)
    psiqui = models.CharField(max_length=1, blank=True, null=True)
    port = models.CharField(max_length=1, blank=True, null=True)
    alte = models.CharField(max_length=1, blank=True, null=True)
    asma = models.CharField(max_length=1, blank=True, null=True)
    epoc = models.CharField(max_length=1, blank=True, null=True)
    hipo = models.CharField(max_length=1, blank=True, null=True)
    diab = models.CharField(max_length=1, blank=True, null=True)
    secue = models.CharField(max_length=1, blank=True, null=True)
    insuf = models.CharField(max_length=1, blank=True, null=True)
    hta = models.CharField(max_length=1, blank=True, null=True)
    medi = models.CharField(max_length=1, blank=True, null=True)
    conv = models.CharField(max_length=1, blank=True, null=True)
    auxilia = models.CharField(max_length=200, blank=True, null=True)
    conclus = models.CharField(max_length=200, blank=True, null=True)
    suste = models.CharField(max_length=1, blank=True, null=True)
    nigta = models.CharField(max_length=1, blank=True, null=True)
    camlibre = models.CharField(max_length=1, blank=True, null=True)
    camlibre1 = models.CharField(max_length=1, blank=True, null=True)
    camlibre2 = models.CharField(max_length=1, blank=True, null=True)
    limita = models.CharField(max_length=1, blank=True, null=True)
    adiadodire = models.CharField(max_length=1, blank=True, null=True)
    adiadoindire = models.CharField(max_length=1, blank=True, null=True)
    anorma = models.CharField(max_length=1, blank=True, null=True)
    pupilas = models.CharField(max_length=1, blank=True, null=True)
    simetria = models.CharField(max_length=1, blank=True, null=True)
    captores = models.CharField(max_length=1, blank=True, null=True)
    crestric = models.CharField(max_length=50, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    antconocimi = models.CharField(max_length=1, blank=True, null=True)
    antapnea = models.CharField(max_length=1, blank=True, null=True)
    antinvolun = models.CharField(max_length=1, blank=True, null=True)
    antdesau = models.CharField(max_length=1, blank=True, null=True)
    anthipart = models.CharField(max_length=1, blank=True, null=True)
    antinscor = models.CharField(max_length=1, blank=True, null=True)
    antcirgcar = models.CharField(max_length=1, blank=True, null=True)
    antdiabmell = models.CharField(max_length=1, blank=True, null=True)
    antinsrenal = models.CharField(max_length=1, blank=True, null=True)
    antabusoal = models.CharField(max_length=1, blank=True, null=True)
    antconsdro = models.CharField(max_length=1, blank=True, null=True)
    antdepre = models.CharField(max_length=1, blank=True, null=True)
    antotros = models.CharField(max_length=200, blank=True, null=True)
    exromb = models.CharField(max_length=1, blank=True, null=True)
    excordcon = models.CharField(max_length=1, blank=True, null=True)
    exotros = models.CharField(max_length=200, blank=True, null=True)
    exmovinvo = models.CharField(max_length=1, blank=True, null=True)
    exaucolum = models.CharField(max_length=1, blank=True, null=True)
    exauextre = models.CharField(max_length=1, blank=True, null=True)
    exaglice = models.CharField(max_length=1, blank=True, null=True)
    exahemo = models.CharField(max_length=1, blank=True, null=True)
    exatoxi = models.CharField(max_length=1, blank=True, null=True)
    exaequi = models.CharField(max_length=1, blank=True, null=True)
    exariesgo = models.CharField(max_length=1, blank=True, null=True)
    exaisque = models.CharField(max_length=1, blank=True, null=True)
    exapsico = models.CharField(max_length=1, blank=True, null=True)
    aptoconfinado = models.CharField(max_length=1, blank=True, null=True)
    noaptoconfinado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estruc'


class EstrucIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    crecomendacion = models.CharField(max_length=200, blank=True, null=True)
    apto = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    noapto = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    conclus = models.CharField(max_length=200, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estruc_iud'


class Estructural(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    crecomendacion = models.CharField(max_length=200, blank=True, null=True)
    apto = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cdesmay = models.CharField(max_length=1, blank=True, null=True)
    cconvul = models.CharField(max_length=1, blank=True, null=True)
    cblanco = models.CharField(max_length=1, blank=True, null=True)
    cnauseas = models.CharField(max_length=1, blank=True, null=True)
    caire = models.CharField(max_length=1, blank=True, null=True)
    czumbido = models.CharField(max_length=1, blank=True, null=True)
    chiperten = models.CharField(max_length=1, blank=True, null=True)
    cantece = models.CharField(max_length=1, blank=True, null=True)
    cactivi = models.CharField(max_length=1, blank=True, null=True)
    cfobia = models.CharField(max_length=1, blank=True, null=True)
    cdiabe = models.CharField(max_length=1, blank=True, null=True)
    cromberg = models.CharField(max_length=1, blank=True, null=True)
    cunterberger = models.CharField(max_length=1, blank=True, null=True)
    cindice = models.CharField(max_length=1, blank=True, null=True)
    cnistagmo = models.CharField(max_length=1, blank=True, null=True)
    coftalmo = models.CharField(max_length=1, blank=True, null=True)
    ccardio = models.CharField(max_length=1, blank=True, null=True)
    cglicemia = models.CharField(max_length=4, blank=True, null=True)
    cekg = models.CharField(max_length=200, blank=True, null=True)
    conclus = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estructural'


class EstructuralIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    crecomendacion = models.CharField(max_length=200, blank=True, null=True)
    apto = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    conclus = models.CharField(max_length=200, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estructural_iud'


class Fracoles(models.Model):
    npunto = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ncod1 = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    ncod2 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    csexo = models.CharField(max_length=1, blank=True, null=True)
    ncod3 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ncod4 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fracoles'


class Fraedad(models.Model):
    npunto = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ncod1 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ncod2 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    csexo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fraedad'


class Frahdl(models.Model):
    npunto = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ncod1 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ncod2 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    csexo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frahdl'


class Frapas(models.Model):
    npunto = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ncod1 = models.CharField(max_length=2, blank=True, null=True)
    ncod2 = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    csexo = models.CharField(max_length=1, blank=True, null=True)
    ncod3 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frapas'


class Fratab(models.Model):
    npunto = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ncod1 = models.CharField(max_length=2, blank=True, null=True)
    ncod2 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    csexo = models.CharField(max_length=1, blank=True, null=True)
    ncod3 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fratab'


class Fratotal(models.Model):
    npunto = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    nriesgo = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    csexo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fratotal'


class Grupo(models.Model):
    cnombre = models.CharField(max_length=50, blank=True, null=True)
    cruc = models.CharField(max_length=11, blank=True, null=True)
    cdireccion = models.TextField(blank=True, null=True)
    ctelefono = models.CharField(max_length=60, blank=True, null=True)
    ccontacto = models.CharField(max_length=100, blank=True, null=True)
    cemail = models.TextField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    cminerales = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupo'


class Historial(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'historial'


class HistorialDet(models.Model):
    id = models.ForeignKey(Historial, db_column='id', blank=True, null=True)
    tfechaini = models.DateTimeField(blank=True, null=True)
    cempresa = models.CharField(max_length=100, blank=True, null=True)
    caltitud = models.CharField(max_length=5, blank=True, null=True)
    cactividad = models.CharField(max_length=100, blank=True, null=True)
    carea = models.CharField(max_length=100, blank=True, null=True)
    cocupa = models.CharField(max_length=100, blank=True, null=True)
    ttiemsup = models.CharField(max_length=30, blank=True, null=True)
    ttiemsub = models.CharField(max_length=30, blank=True, null=True)
    cpelig = models.CharField(max_length=100, blank=True, null=True)
    clentes = models.CharField(max_length=10, blank=True, null=True)
    item = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    iddet = models.AutoField(primary_key=True)
    czapatos = models.CharField(max_length=10, blank=True, null=True)
    ccasco = models.CharField(max_length=10, blank=True, null=True)
    cguantes = models.CharField(max_length=10, blank=True, null=True)
    ctapones = models.CharField(max_length=10, blank=True, null=True)
    crespir = models.CharField(max_length=10, blank=True, null=True)
    clugar = models.CharField(max_length=30, blank=True, null=True)
    cropa = models.CharField(max_length=10, blank=True, null=True)
    csinepp = models.CharField(max_length=10, blank=True, null=True)
    tfechafin = models.DateTimeField(blank=True, null=True)
    ccargo = models.CharField(max_length=80, blank=True, null=True)
    cproyecto = models.CharField(max_length=50, blank=True, null=True)
    naltitud = models.CharField(max_length=2, blank=True, null=True)
    criesgos = models.CharField(max_length=2, blank=True, null=True)
    choraexp = models.CharField(max_length=6, blank=True, null=True)
    cporuso = models.CharField(max_length=2, blank=True, null=True)
    ccentromedico = models.CharField(max_length=100, blank=True, null=True)
    tfecharet = models.DateTimeField(blank=True, null=True)
    challazgos = models.CharField(max_length=200, blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_det'


class HistorialDetIud(models.Model):
    idop = models.CharField(max_length=1)
    idsimon = models.IntegerField(blank=True, null=True)
    iddetsimon = models.IntegerField(blank=True, null=True)
    item = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cempresa = models.CharField(max_length=100, blank=True, null=True)
    clugar = models.CharField(max_length=20, blank=True, null=True)
    cocupa = models.CharField(max_length=100, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_det_iud'


class HistorialIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_iud'


class Institucion(models.Model):
    razonsocial = models.CharField(max_length=40)
    ruc = models.CharField(max_length=11)
    direccion = models.CharField(max_length=70)
    distrito = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fax = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    notas = models.TextField(blank=True, null=True)
    dominio = models.CharField(max_length=100, blank=True, null=True)
    bimagen = models.BinaryField(blank=True, null=True)
    cmime = models.CharField(max_length=20, blank=True, null=True)
    cadena = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institucion'


class Interconsultam(models.Model):
    id = models.AutoField(primary_key=True)
    cnombre = models.CharField(max_length=40, blank=True, null=True)
    cespi = models.CharField(max_length=30, blank=True, null=True)
    ccmp = models.CharField(max_length=6, blank=True, null=True)
    crei = models.CharField(max_length=6, blank=True, null=True)
    ctelefono = models.CharField(max_length=10, blank=True, null=True)
    ccelular = models.CharField(max_length=10, blank=True, null=True)
    cdireccion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interconsultam'


class Laboratorio(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    nshemo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    nshema = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nsgrupo = models.CharField(max_length=6, blank=True, null=True)
    nsfactorrh = models.CharField(max_length=1, blank=True, null=True)
    nsglucosa = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    nscreatinina = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    nstgo = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    nstgp = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    nsggtp = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    nscolesterol = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    nshdl = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    nsldl = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    nstrigliceridos = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    nsacidourico = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nsvdrlrpr = models.CharField(max_length=26, blank=True, null=True)
    nsplaquetas = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True)
    nshemoneutrofilos = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    nshemojuveniles = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    nshemoabastonados = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nshemoeosinofilos = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    nshemobasofilos = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    nshemolinfocitos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nshemoreticulositos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nsespplomo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nsespmercurio = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nsespmarihuana = models.CharField(max_length=26, blank=True, null=True)
    nsespcocaina = models.CharField(max_length=26, blank=True, null=True)
    nsesphepatitisa = models.CharField(max_length=26, blank=True, null=True)
    nsesphiv = models.CharField(max_length=26, blank=True, null=True)
    noexsecilindros = models.CharField(max_length=26, blank=True, null=True)
    noprotein = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nomahuana = models.CharField(max_length=26, blank=True, null=True)
    nococaina = models.CharField(max_length=26, blank=True, null=True)
    noexsecelulas = models.CharField(max_length=26, blank=True, null=True)
    nhdirecto = models.TextField(blank=True, null=True)
    nhparasitologico = models.TextField(blank=True, null=True)
    nebk = models.CharField(max_length=26, blank=True, null=True)
    neraspado = models.CharField(max_length=26, blank=True, null=True)
    nepap = models.TextField(blank=True, null=True)
    nshemonroleuco = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True)
    nsesphepatitisb = models.CharField(max_length=26, blank=True, null=True)
    nseshepatitisc = models.CharField(max_length=26, blank=True, null=True)
    noexsebacterias = models.CharField(max_length=26, blank=True, null=True)
    noexsepiocitos = models.CharField(max_length=26, blank=True, null=True)
    noexseph = models.CharField(max_length=26, blank=True, null=True)
    noexseaspecto = models.CharField(max_length=26, blank=True, null=True)
    noexsecolor = models.CharField(max_length=26, blank=True, null=True)
    noexseolor = models.CharField(max_length=26, blank=True, null=True)
    noexsehematies = models.CharField(max_length=26, blank=True, null=True)
    noexseleucitos = models.CharField(max_length=26, blank=True, null=True)
    noexsecristales = models.CharField(max_length=26, blank=True, null=True)
    noexdensidad = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    noexseotros = models.CharField(max_length=26, blank=True, null=True)
    noexsereaccion = models.CharField(max_length=26, blank=True, null=True)
    noexciproteinas = models.CharField(max_length=26, blank=True, null=True)
    noexcinitrotos = models.CharField(max_length=26, blank=True, null=True)
    noexciglucosa = models.CharField(max_length=26, blank=True, null=True)
    noexcisangre = models.CharField(max_length=26, blank=True, null=True)
    noexciurobilina = models.CharField(max_length=26, blank=True, null=True)
    noexcicuerposcet = models.CharField(max_length=26, blank=True, null=True)
    noexcipigbiliares = models.CharField(max_length=26, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    nshemomielocitos = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    cobservacion = models.TextField(blank=True, null=True)
    cdiagnostico = models.CharField(max_length=100, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    nobenzodiazepina = models.CharField(max_length=26, blank=True, null=True)
    noanfetaminas = models.CharField(max_length=26, blank=True, null=True)
    nometaanfetaminas = models.CharField(max_length=26, blank=True, null=True)
    noparasito = models.CharField(max_length=100, blank=True, null=True)
    nobkesputo = models.CharField(max_length=26, blank=True, null=True)
    nocorpo = models.CharField(max_length=100, blank=True, null=True)
    nowidal = models.CharField(max_length=50, blank=True, null=True)
    nohepaigm = models.CharField(max_length=26, blank=True, null=True)
    nssegmentados = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nsmonocitos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nshemoglobina = models.CharField(max_length=26, blank=True, null=True)
    nspsa = models.CharField(max_length=26, blank=True, null=True)
    nspregnosticon = models.CharField(max_length=26, blank=True, null=True)
    nsvelsed = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    nsreticulositos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nsvsg = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    nsanticuerpos = models.CharField(max_length=26, blank=True, null=True)
    nometanefrina = models.CharField(max_length=26, blank=True, null=True)
    nofenilciclyna = models.CharField(max_length=26, blank=True, null=True)
    ncelepite = models.CharField(max_length=26, blank=True, null=True)
    nscromo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nscadmio = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nstiempo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ncolesti = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hcgbeta = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cpregnostico = models.CharField(max_length=26, blank=True, null=True)
    orinadiag = models.CharField(max_length=26, blank=True, null=True)
    hemodiag = models.CharField(max_length=26, blank=True, null=True)
    nsespanfe = models.CharField(max_length=26, blank=True, null=True)
    nsespbenzo = models.CharField(max_length=26, blank=True, null=True)
    npap = models.CharField(max_length=26, blank=True, null=True)
    npapobser = models.CharField(max_length=26, blank=True, null=True)
    npara1 = models.CharField(max_length=26, blank=True, null=True)
    npara2 = models.CharField(max_length=26, blank=True, null=True)
    npara3 = models.CharField(max_length=26, blank=True, null=True)
    nagsubhb = models.CharField(max_length=26, blank=True, null=True)
    baciloscopia1 = models.CharField(max_length=26, blank=True, null=True)
    baciloscopia2 = models.CharField(max_length=26, blank=True, null=True)
    baciloscopia3 = models.CharField(max_length=26, blank=True, null=True)
    ppd = models.CharField(max_length=26, blank=True, null=True)
    ncopropa1 = models.CharField(max_length=26, blank=True, null=True)
    ncopropa2 = models.CharField(max_length=26, blank=True, null=True)
    ncopropa3 = models.CharField(max_length=26, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    aglutinacion = models.CharField(max_length=26, blank=True, null=True)
    cultinazo = models.CharField(max_length=30, blank=True, null=True)
    nsesphiv2 = models.CharField(max_length=26, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laboratorio'


class LaboratorioIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cobservacion = models.TextField(blank=True, null=True)
    cdiagnostico = models.CharField(max_length=50, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=50, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laboratorio_iud'


class Labsmu(models.Model):
    codex = models.CharField(primary_key=True, max_length=150)
    nombre = models.CharField(max_length=150, blank=True, null=True)
    numlabs = models.IntegerField(blank=True, null=True)
    nomlabs = models.CharField(max_length=150, blank=True, null=True)
    tipodato = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labsmu'


class Medicos(models.Model):
    id = models.AutoField(primary_key=True)
    especialidad = models.CharField(max_length=2, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    tfecha = models.DateField(blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicos'


class Ocupacional(models.Model):
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    ccomentario = models.TextField(blank=True, null=True)
    crecomendaciones = models.TextField(blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    csindrome = models.CharField(max_length=41, blank=True, null=True)
    cframinga = models.CharField(max_length=10, blank=True, null=True)
    tfechare = models.DateField(blank=True, null=True)
    cmedico = models.CharField(max_length=100, blank=True, null=True)
    cconsultorio = models.TextField(blank=True, null=True)
    cobservaciones = models.TextField(blank=True, null=True)
    crazonobser = models.TextField(blank=True, null=True)
    year = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    tfechaca = models.DateField(blank=True, null=True)
    thorain = models.CharField(max_length=8, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    captomedico = models.CharField(max_length=10, blank=True, null=True)
    ccie10 = models.CharField(max_length=200, blank=True, null=True)
    cdiagnosticobambas = models.TextField(blank=True, null=True)
    crestricciones = models.TextField(blank=True, null=True)
    crecomendacionesbambas = models.TextField(blank=True, null=True)
    tfecha2 = models.DateTimeField(blank=True, null=True)
    cinterconsultasbambas = models.TextField(blank=True, null=True)
    cmedicobambas = models.CharField(max_length=5, blank=True, null=True)
    crestricciones1 = models.CharField(max_length=1, blank=True, null=True)
    crestricciones2 = models.CharField(max_length=1, blank=True, null=True)
    crestricciones3 = models.CharField(max_length=1, blank=True, null=True)
    crestricciones4 = models.CharField(max_length=1, blank=True, null=True)
    crestricciones5 = models.CharField(max_length=1, blank=True, null=True)
    crestricciones6 = models.CharField(max_length=1, blank=True, null=True)
    crestricciones7 = models.CharField(max_length=1, blank=True, null=True)
    crestricciones8 = models.CharField(max_length=1, blank=True, null=True)
    crestricciones9 = models.CharField(max_length=1, blank=True, null=True)
    crestricciones10 = models.CharField(max_length=1, blank=True, null=True)
    crestricciones11 = models.CharField(max_length=100, blank=True, null=True)
    sportal = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cdiagcosapi = models.TextField(blank=True, null=True)
    cod_cie10 = models.CharField(max_length=100, blank=True, null=True)
    nom_cie10 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocupacional'


class OcupacionalDet(models.Model):
    id = models.ForeignKey(Ocupacional, db_column='id', blank=True, null=True)
    iddet = models.AutoField(primary_key=True)
    tfechaini = models.DateTimeField(blank=True, null=True)
    tfechare = models.DateField(blank=True, null=True)
    cmedico = models.CharField(max_length=100, blank=True, null=True)
    cconsultorio = models.TextField(blank=True, null=True)
    thorain = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocupacional_det'


class OcupacionalIud(models.Model):
    idop = models.CharField(max_length=1, blank=True, null=True)
    idchistoria = models.CharField(max_length=16)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    ccomentario = models.TextField(blank=True, null=True)
    cobservaciones = models.TextField(blank=True, null=True)
    crazonobser = models.TextField(blank=True, null=True)
    tfechaca = models.DateField(blank=True, null=True)
    tfecha2 = models.DateTimeField(blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)
    cusers = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocupacional_iud'


class Odontograma(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cpieza18 = models.CharField(max_length=10, blank=True, null=True)
    cpieza17 = models.CharField(max_length=10, blank=True, null=True)
    cpieza16 = models.CharField(max_length=10, blank=True, null=True)
    cpieza15 = models.CharField(max_length=10, blank=True, null=True)
    cpieza14 = models.CharField(max_length=10, blank=True, null=True)
    cpieza13 = models.CharField(max_length=10, blank=True, null=True)
    cpieza12 = models.CharField(max_length=10, blank=True, null=True)
    cpieza11 = models.CharField(max_length=10, blank=True, null=True)
    cpieza21 = models.CharField(max_length=10, blank=True, null=True)
    cpieza22 = models.CharField(max_length=10, blank=True, null=True)
    cpieza23 = models.CharField(max_length=10, blank=True, null=True)
    cpieza24 = models.CharField(max_length=10, blank=True, null=True)
    cpieza25 = models.CharField(max_length=10, blank=True, null=True)
    cpieza26 = models.CharField(max_length=10, blank=True, null=True)
    cpieza27 = models.CharField(max_length=10, blank=True, null=True)
    cpieza28 = models.CharField(max_length=10, blank=True, null=True)
    cpieza48 = models.CharField(max_length=10, blank=True, null=True)
    cpieza47 = models.CharField(max_length=10, blank=True, null=True)
    cpieza46 = models.CharField(max_length=10, blank=True, null=True)
    cpieza45 = models.CharField(max_length=10, blank=True, null=True)
    cpieza44 = models.CharField(max_length=10, blank=True, null=True)
    cpieza43 = models.CharField(max_length=10, blank=True, null=True)
    cpieza42 = models.CharField(max_length=10, blank=True, null=True)
    cpieza41 = models.CharField(max_length=10, blank=True, null=True)
    cpieza31 = models.CharField(max_length=10, blank=True, null=True)
    cpieza32 = models.CharField(max_length=10, blank=True, null=True)
    cpieza33 = models.CharField(max_length=10, blank=True, null=True)
    cpieza34 = models.CharField(max_length=10, blank=True, null=True)
    cpieza35 = models.CharField(max_length=10, blank=True, null=True)
    cpieza36 = models.CharField(max_length=10, blank=True, null=True)
    cpieza37 = models.CharField(max_length=10, blank=True, null=True)
    cpieza38 = models.CharField(max_length=10, blank=True, null=True)
    cpieza55 = models.CharField(max_length=4, blank=True, null=True)
    cpieza54 = models.CharField(max_length=4, blank=True, null=True)
    cpieza53 = models.CharField(max_length=4, blank=True, null=True)
    cpieza52 = models.CharField(max_length=4, blank=True, null=True)
    cpieza51 = models.CharField(max_length=4, blank=True, null=True)
    cpieza61 = models.CharField(max_length=4, blank=True, null=True)
    cpieza62 = models.CharField(max_length=4, blank=True, null=True)
    cpieza63 = models.CharField(max_length=4, blank=True, null=True)
    cpieza64 = models.CharField(max_length=4, blank=True, null=True)
    cpieza65 = models.CharField(max_length=4, blank=True, null=True)
    cpieza85 = models.CharField(max_length=4, blank=True, null=True)
    cpieza84 = models.CharField(max_length=4, blank=True, null=True)
    cpieza83 = models.CharField(max_length=4, blank=True, null=True)
    cpieza82 = models.CharField(max_length=4, blank=True, null=True)
    cpieza81 = models.CharField(max_length=4, blank=True, null=True)
    cpieza71 = models.CharField(max_length=4, blank=True, null=True)
    cpieza72 = models.CharField(max_length=4, blank=True, null=True)
    cpieza73 = models.CharField(max_length=4, blank=True, null=True)
    cpieza74 = models.CharField(max_length=4, blank=True, null=True)
    cpieza75 = models.CharField(max_length=4, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cobservaciones = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    cmal = models.CharField(max_length=200, blank=True, null=True)
    cfalta = models.CharField(max_length=200, blank=True, null=True)
    cobturada = models.CharField(max_length=200, blank=True, null=True)
    ccie10 = models.CharField(max_length=8, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cdiagnosticoscom = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'odontograma'


class OdontogramaIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cobservaciones = models.TextField(blank=True, null=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cdiagnosticoscom = models.TextField(blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'odontograma_iud'


class Oftalmologia(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.CharField(max_length=80, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    clentes = models.CharField(max_length=1, blank=True, null=True)
    cpicos = models.CharField(max_length=1, blank=True, null=True)
    cquemazon = models.CharField(max_length=1, blank=True, null=True)
    csensacion = models.CharField(max_length=1, blank=True, null=True)
    cvisionb = models.CharField(max_length=1, blank=True, null=True)
    ccefalea = models.CharField(max_length=1, blank=True, null=True)
    cdeslumbramiento = models.CharField(max_length=1, blank=True, null=True)
    cotros = models.CharField(max_length=30, blank=True, null=True)
    cparpados = models.CharField(max_length=1, blank=True, null=True)
    cpolo = models.CharField(max_length=1, blank=True, null=True)
    cmotilidadint = models.CharField(max_length=1, blank=True, null=True)
    cmotilidadext = models.CharField(max_length=1, blank=True, null=True)
    cvisioncolores = models.CharField(max_length=1, blank=True, null=True)
    cvisionprofundi = models.CharField(max_length=1, blank=True, null=True)
    creflejopu = models.CharField(max_length=1, blank=True, null=True)
    ccampimetria = models.CharField(max_length=1, blank=True, null=True)
    cdescripcion = models.TextField(blank=True, null=True)
    csinvileod = models.CharField(max_length=6, blank=True, null=True)
    csinvileoi = models.CharField(max_length=6, blank=True, null=True)
    csinviceod = models.CharField(max_length=6, blank=True, null=True)
    csinviceoi = models.CharField(max_length=6, blank=True, null=True)
    cconevileod = models.CharField(max_length=6, blank=True, null=True)
    cconevileoi = models.CharField(max_length=6, blank=True, null=True)
    cconeviceod = models.CharField(max_length=6, blank=True, null=True)
    cconeviceoi = models.CharField(max_length=6, blank=True, null=True)
    cconvileod = models.CharField(max_length=6, blank=True, null=True)
    cconvileoi = models.CharField(max_length=6, blank=True, null=True)
    cconviceod = models.CharField(max_length=6, blank=True, null=True)
    cconviceoi = models.CharField(max_length=6, blank=True, null=True)
    ctonood = models.CharField(max_length=6, blank=True, null=True)
    ctonooi = models.CharField(max_length=6, blank=True, null=True)
    cbiomicro = models.CharField(max_length=30, blank=True, null=True)
    cgonio = models.CharField(max_length=20, blank=True, null=True)
    cfondo = models.CharField(max_length=20, blank=True, null=True)
    codesfericolejos = models.CharField(max_length=5, blank=True, null=True)
    codcilindrolejos = models.CharField(max_length=5, blank=True, null=True)
    codejeslejos = models.CharField(max_length=5, blank=True, null=True)
    coddiplejos = models.CharField(max_length=5, blank=True, null=True)
    coiesfericolejos = models.CharField(max_length=5, blank=True, null=True)
    coicilindrolejos = models.CharField(max_length=5, blank=True, null=True)
    coiejeslejos = models.CharField(max_length=5, blank=True, null=True)
    coidiplejos = models.CharField(max_length=5, blank=True, null=True)
    cadesfericolejos = models.CharField(max_length=5, blank=True, null=True)
    cadcilindrolejos = models.CharField(max_length=5, blank=True, null=True)
    cadejeslejos = models.CharField(max_length=5, blank=True, null=True)
    caddiplejos = models.CharField(max_length=5, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    cexposicion = models.TextField(blank=True, null=True)
    cpuntocon = models.CharField(max_length=1, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    year = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    cexplicacion = models.TextField(blank=True, null=True)
    cdiagnosticood = models.CharField(max_length=100, blank=True, null=True)
    cdiagnosticooi = models.CharField(max_length=100, blank=True, null=True)
    ccie10 = models.CharField(max_length=7, blank=True, null=True)
    ccondiag = models.CharField(max_length=3, blank=True, null=True)
    ccondiag1 = models.CharField(max_length=3, blank=True, null=True)
    cfondooi = models.CharField(max_length=100, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cdiagnosticoscom = models.TextField(blank=True, null=True)
    clectura = models.CharField(max_length=2, blank=True, null=True)
    idcalibracion = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cadesferico = models.CharField(max_length=5, blank=True, null=True)
    cadcilindro = models.CharField(max_length=5, blank=True, null=True)
    cadeje = models.CharField(max_length=5, blank=True, null=True)
    caddip = models.CharField(max_length=5, blank=True, null=True)
    rpupilares = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oftalmologia'


class OftalmologiaIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.CharField(max_length=80, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    cdiagnosticood = models.CharField(max_length=100, blank=True, null=True)
    cdiagnosticooi = models.CharField(max_length=100, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oftalmologia_iud'


class Operadormovil(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    crisis = models.CharField(max_length=1, blank=True, null=True)
    movimi = models.CharField(max_length=1, blank=True, null=True)
    diabe = models.CharField(max_length=1, blank=True, null=True)
    insufi = models.CharField(max_length=1, blank=True, null=True)
    consumo = models.CharField(max_length=1, blank=True, null=True)
    arritmia = models.CharField(max_length=1, blank=True, null=True)
    portador = models.CharField(max_length=1, blank=True, null=True)
    ausensia = models.CharField(max_length=1, blank=True, null=True)
    medicacion = models.CharField(max_length=1, blank=True, null=True)
    renal = models.CharField(max_length=1, blank=True, null=True)
    coronaria = models.CharField(max_length=1, blank=True, null=True)
    diplopia = models.CharField(max_length=1, blank=True, null=True)
    hipertension = models.CharField(max_length=1, blank=True, null=True)
    protesis = models.CharField(max_length=1, blank=True, null=True)
    intranquilidad = models.CharField(max_length=1, blank=True, null=True)
    labilidad = models.CharField(max_length=1, blank=True, null=True)
    fobias = models.CharField(max_length=1, blank=True, null=True)
    sueno = models.CharField(max_length=1, blank=True, null=True)
    peso = models.CharField(max_length=1, blank=True, null=True)
    drogas2 = models.CharField(max_length=1, blank=True, null=True)
    funciones = models.CharField(max_length=1, blank=True, null=True)
    aparatolocomotor = models.CharField(max_length=1, blank=True, null=True)
    muscular = models.CharField(max_length=1, blank=True, null=True)
    vestibulares = models.CharField(max_length=1, blank=True, null=True)
    agudeza = models.CharField(max_length=1, blank=True, null=True)
    cromatica = models.CharField(max_length=1, blank=True, null=True)
    estereoscopica = models.CharField(max_length=1, blank=True, null=True)
    umbral = models.CharField(max_length=1, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    capto = models.CharField(max_length=1, blank=True, null=True)
    cobservacion = models.TextField(blank=True, null=True)
    cpor2 = models.CharField(max_length=1, blank=True, null=True)
    cpor1 = models.CharField(max_length=1, blank=True, null=True)
    cnoapto = models.CharField(max_length=1, blank=True, null=True)
    cflag = models.CharField(max_length=1, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operadormovil'


class Osteomuscular(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    clevanta = models.CharField(max_length=1, blank=True, null=True)
    cempuja = models.CharField(max_length=1, blank=True, null=True)
    ctiempoexp = models.CharField(max_length=3, blank=True, null=True)
    cvoldif = models.CharField(max_length=1, blank=True, null=True)
    cequiines = models.CharField(max_length=1, blank=True, null=True)
    cmandis = models.CharField(max_length=1, blank=True, null=True)
    cexitori = models.CharField(max_length=1, blank=True, null=True)
    cexipos = models.CharField(max_length=1, blank=True, null=True)
    ccueinse = models.CharField(max_length=1, blank=True, null=True)
    calzar = models.CharField(max_length=1, blank=True, null=True)
    cespacio = models.CharField(max_length=1, blank=True, null=True)
    csueloir = models.CharField(max_length=1, blank=True, null=True)
    caltura = models.CharField(max_length=1, blank=True, null=True)
    cpostura = models.CharField(max_length=1, blank=True, null=True)
    cdesnivel = models.CharField(max_length=1, blank=True, null=True)
    csuelo = models.CharField(max_length=1, blank=True, null=True)
    cvibracion = models.CharField(max_length=1, blank=True, null=True)
    ctempera = models.CharField(max_length=1, blank=True, null=True)
    cesfuerzosfisicos = models.CharField(max_length=1, blank=True, null=True)
    cperiodoins = models.CharField(max_length=1, blank=True, null=True)
    cmarcha = models.CharField(max_length=3, blank=True, null=True)
    canomalias = models.CharField(max_length=3, blank=True, null=True)
    csimetria = models.CharField(max_length=3, blank=True, null=True)
    ccolumna = models.CharField(max_length=3, blank=True, null=True)
    cpalpacionmus = models.CharField(max_length=3, blank=True, null=True)
    cpalpacion = models.CharField(max_length=3, blank=True, null=True)
    cpercucion = models.CharField(max_length=3, blank=True, null=True)
    csignoslase = models.CharField(max_length=3, blank=True, null=True)
    csignoscho = models.CharField(max_length=3, blank=True, null=True)
    carticulaciones = models.CharField(max_length=3, blank=True, null=True)
    chombro = models.CharField(max_length=3, blank=True, null=True)
    cmunecamano = models.CharField(max_length=3, blank=True, null=True)
    chombroabsuccion = models.CharField(max_length=2, blank=True, null=True)
    chombroadduccion = models.CharField(max_length=2, blank=True, null=True)
    chombroflexion = models.CharField(max_length=2, blank=True, null=True)
    chombroextension = models.CharField(max_length=2, blank=True, null=True)
    chombrorotaex = models.CharField(max_length=2, blank=True, null=True)
    chombrorotain = models.CharField(max_length=2, blank=True, null=True)
    ccodoabsuccion = models.CharField(max_length=2, blank=True, null=True)
    ccodoadduccion = models.CharField(max_length=2, blank=True, null=True)
    ccodoflexion = models.CharField(max_length=2, blank=True, null=True)
    ccodoextension = models.CharField(max_length=2, blank=True, null=True)
    ccodorotaex = models.CharField(max_length=2, blank=True, null=True)
    ccodorotain = models.CharField(max_length=2, blank=True, null=True)
    cmunecaabsuccion = models.CharField(max_length=2, blank=True, null=True)
    cmunecaadduccion = models.CharField(max_length=2, blank=True, null=True)
    cmunecaflexion = models.CharField(max_length=2, blank=True, null=True)
    cmunecaextension = models.CharField(max_length=2, blank=True, null=True)
    cmunecarotaex = models.CharField(max_length=2, blank=True, null=True)
    cmunecarotain = models.CharField(max_length=2, blank=True, null=True)
    ccaderaabsuccion = models.CharField(max_length=2, blank=True, null=True)
    ccaderaadduccion = models.CharField(max_length=2, blank=True, null=True)
    ccaderaflexion = models.CharField(max_length=2, blank=True, null=True)
    ccaderaextension = models.CharField(max_length=2, blank=True, null=True)
    ccaderarotaex = models.CharField(max_length=2, blank=True, null=True)
    ccaderarotain = models.CharField(max_length=2, blank=True, null=True)
    crodillaabsuccion = models.CharField(max_length=2, blank=True, null=True)
    crodillaadduccion = models.CharField(max_length=2, blank=True, null=True)
    crodillaflexion = models.CharField(max_length=2, blank=True, null=True)
    crodillaextension = models.CharField(max_length=2, blank=True, null=True)
    crodillarotaex = models.CharField(max_length=2, blank=True, null=True)
    crodillarotain = models.CharField(max_length=2, blank=True, null=True)
    ctobilloabsuccion = models.CharField(max_length=2, blank=True, null=True)
    ctobilloadduccion = models.CharField(max_length=2, blank=True, null=True)
    ctobilloflexion = models.CharField(max_length=2, blank=True, null=True)
    ctobilloextension = models.CharField(max_length=2, blank=True, null=True)
    ctobillorotaex = models.CharField(max_length=2, blank=True, null=True)
    ctobillorotain = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    cpeso = models.CharField(max_length=3, blank=True, null=True)
    cdistancia = models.CharField(max_length=1, blank=True, null=True)
    critmo = models.CharField(max_length=1, blank=True, null=True)
    cflexibab = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ccadera = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cmuslo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cabdomen = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cabduccionhombro = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cadduccionhombro = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    crotacionext = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    crotacionexthom = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ctotal = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ctotal2 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    crecomendaciones = models.TextField(blank=True, null=True)
    ccie10 = models.CharField(max_length=20, blank=True, null=True)
    ccomentario = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'osteomuscular'


class OsteomuscularIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    crecomendaciones = models.TextField(blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'osteomuscular_iud'


class Perfiles(models.Model):
    tfecha = models.DateTimeField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)
    dfecha = models.DateField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    cempresa = models.CharField(max_length=11, blank=True, null=True)
    cpuesto = models.CharField(max_length=40, blank=True, null=True)
    c1 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c2 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c3 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c4 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c5 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c6 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c7 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c8 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c9 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c10 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c11 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c12 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c13 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c14 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c15 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c16 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c17 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c18 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c19 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    cgrupo = models.IntegerField(blank=True, null=True)
    cbase = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    csexo = models.CharField(max_length=2, blank=True, null=True)
    cedad = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    cedad2 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ccargo = models.TextField(blank=True, null=True)
    ccerro = models.CharField(max_length=50, blank=True, null=True)
    cidcargo = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    cobservaciones = models.CharField(max_length=100, blank=True, null=True)
    visio14 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfiles'


class PerfilesIud(models.Model):
    idop = models.CharField(max_length=1)
    idcempresa = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfiles_iud'


class Perfileslab(models.Model):
    tfecha = models.DateTimeField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)
    dfecha = models.DateField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    c1 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c2 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c3 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c4 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c5 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c6 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c7 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c8 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c9 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c10 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c11 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c12 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c13 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c14 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c15 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c16 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c17 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c18 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c19 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    cperfil = models.IntegerField(blank=True, null=True)
    c20 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c21 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c22 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c23 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c24 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c25 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c26 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c27 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c28 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c29 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c30 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c31 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c32 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c33 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c34 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c35 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c36 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c37 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c38 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c39 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c40 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c41 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c42 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c44 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c45 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c43 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c46 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c47 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c48 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c49 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c50 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c51 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    c52 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfileslab'


class Personal(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40, blank=True, null=True)
    documento = models.CharField(max_length=20, blank=True, null=True)
    fechaingreso = models.DateField(blank=True, null=True)
    notas = models.CharField(max_length=50)
    cargo = models.CharField(max_length=3, blank=True, null=True)
    afp = models.CharField(max_length=15, blank=True, null=True)
    afpnumero = models.CharField(max_length=16, blank=True, null=True)
    essalud = models.CharField(max_length=16, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    activa = models.CharField(max_length=1, blank=True, null=True)
    login = models.CharField(unique=True, max_length=4)
    pwd = models.CharField(max_length=10)
    id_nivel = models.CharField(max_length=2, blank=True, null=True)
    activo = models.CharField(max_length=1, blank=True, null=True)
    licen_con = models.CharField(max_length=15, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=5)
    aliasusr = models.CharField(max_length=40, blank=True, null=True)
    id_unidad = models.IntegerField(blank=True, null=True)
    id_grupo = models.IntegerField(blank=True, null=True)
    id_creo = models.IntegerField(blank=True, null=True)
    f_ingreso = models.DateField(blank=True, null=True)
    id_modifico = models.IntegerField(blank=True, null=True)
    f_baja = models.DateField(blank=True, null=True)
    ult_modif = models.DateField(blank=True, null=True)
    ult_acceso = models.DateField(blank=True, null=True)
    ult_cambioc = models.DateField(blank=True, null=True)
    ncambios = models.IntegerField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    habilitado = models.CharField(max_length=1, blank=True, null=True)
    cdatos = models.CharField(max_length=100, blank=True, null=True)
    ccolegio = models.CharField(max_length=10, blank=True, null=True)
    ccargo = models.CharField(max_length=3, blank=True, null=True)
    id_valor = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'personal'


class Psico(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    enfermedades = models.TextField()
    otros = models.TextField(blank=True, null=True)
    critmo = models.CharField(max_length=3, blank=True, null=True)
    ctiempo = models.CharField(max_length=3, blank=True, null=True)
    ctono = models.CharField(max_length=3, blank=True, null=True)
    cespacio = models.CharField(max_length=3, blank=True, null=True)
    carti = models.CharField(max_length=3, blank=True, null=True)
    cpersona = models.CharField(max_length=3, blank=True, null=True)
    cpresen = models.CharField(max_length=3, blank=True, null=True)
    cpostura = models.CharField(max_length=3, blank=True, null=True)
    habitos = models.CharField(max_length=3, blank=True, null=True)
    cintelectual = models.TextField(blank=True, null=True)
    cmini = models.CharField(max_length=2, blank=True, null=True)
    cminimult = models.CharField(max_length=2, blank=True, null=True)
    clluvia = models.CharField(max_length=2, blank=True, null=True)
    cbenton = models.CharField(max_length=2, blank=True, null=True)
    cescala = models.CharField(max_length=2, blank=True, null=True)
    cmaslach = models.CharField(max_length=2, blank=True, null=True)
    cfobia = models.CharField(max_length=2, blank=True, null=True)
    cpersonalidad = models.TextField(blank=True, null=True)
    laboral = models.TextField(blank=True, null=True)
    clucidez = models.TextField(blank=True, null=True)
    cpensamiento = models.TextField(blank=True, null=True)
    cpersepcion = models.TextField(blank=True, null=True)
    cmemoria = models.CharField(max_length=3, blank=True, null=True)
    cinteligencia = models.CharField(max_length=3, blank=True, null=True)
    capetito = models.TextField(blank=True, null=True)
    csueno = models.TextField(blank=True, null=True)
    crecomendacion = models.TextField(blank=True, null=True)
    cestaapto = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cestanoapto = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cestaaptocon = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cintelectual1 = models.TextField(blank=True, null=True)
    cpersonalidad1 = models.TextField(blank=True, null=True)
    claboral1 = models.TextField(blank=True, null=True)
    cagorafobia = models.TextField(blank=True, null=True)
    ctest = models.CharField(max_length=100, blank=True, null=True)
    cconducta = models.CharField(max_length=2, blank=True, null=True)
    cproyectivo = models.CharField(max_length=2, blank=True, null=True)
    cmemoria1 = models.CharField(max_length=2, blank=True, null=True)
    cmemoria2 = models.CharField(max_length=2, blank=True, null=True)
    cevaluacio = models.CharField(max_length=1, blank=True, null=True)
    cpruebas = models.CharField(max_length=100, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=180, blank=True, null=True)
    canual = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'psico'


class Psicologia1(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    c1 = models.CharField(max_length=1, blank=True, null=True)
    c2 = models.CharField(max_length=1, blank=True, null=True)
    c3 = models.CharField(max_length=1, blank=True, null=True)
    c4 = models.CharField(max_length=1, blank=True, null=True)
    c5 = models.CharField(max_length=1, blank=True, null=True)
    c6 = models.CharField(max_length=1, blank=True, null=True)
    c7 = models.CharField(max_length=1, blank=True, null=True)
    c8 = models.CharField(max_length=1, blank=True, null=True)
    c9 = models.CharField(max_length=1, blank=True, null=True)
    c10 = models.CharField(max_length=1, blank=True, null=True)
    c11 = models.CharField(max_length=1, blank=True, null=True)
    c12 = models.CharField(max_length=1, blank=True, null=True)
    c13 = models.CharField(max_length=1, blank=True, null=True)
    c14 = models.CharField(max_length=1, blank=True, null=True)
    c15 = models.CharField(max_length=1, blank=True, null=True)
    c16 = models.CharField(max_length=1, blank=True, null=True)
    c17 = models.CharField(max_length=1, blank=True, null=True)
    c18 = models.CharField(max_length=1, blank=True, null=True)
    c19 = models.CharField(max_length=1, blank=True, null=True)
    c20 = models.CharField(max_length=1, blank=True, null=True)
    c21 = models.CharField(max_length=1, blank=True, null=True)
    c22 = models.CharField(max_length=1, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cobservaciones = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    cmal = models.CharField(max_length=100, blank=True, null=True)
    cfalta = models.CharField(max_length=100, blank=True, null=True)
    year1 = models.CharField(max_length=4, blank=True, null=True)
    cdiagnostico2 = models.TextField(blank=True, null=True)
    cdiagnostico1 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'psicologia1'


class Psicologia11(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    c1 = models.CharField(max_length=1, blank=True, null=True)
    c2 = models.CharField(max_length=1, blank=True, null=True)
    c3 = models.CharField(max_length=1, blank=True, null=True)
    c4 = models.CharField(max_length=1, blank=True, null=True)
    c5 = models.CharField(max_length=1, blank=True, null=True)
    c6 = models.CharField(max_length=1, blank=True, null=True)
    c7 = models.CharField(max_length=1, blank=True, null=True)
    c8 = models.CharField(max_length=1, blank=True, null=True)
    c9 = models.CharField(max_length=1, blank=True, null=True)
    c10 = models.CharField(max_length=1, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cobservaciones = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    year1 = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'psicologia11'


class Psicologia2(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    c11 = models.CharField(max_length=2, blank=True, null=True)
    c12 = models.CharField(max_length=2, blank=True, null=True)
    c13 = models.CharField(max_length=2, blank=True, null=True)
    c14 = models.CharField(max_length=2, blank=True, null=True)
    c15 = models.CharField(max_length=2, blank=True, null=True)
    c16 = models.CharField(max_length=2, blank=True, null=True)
    c17 = models.CharField(max_length=2, blank=True, null=True)
    c18 = models.CharField(max_length=2, blank=True, null=True)
    c19 = models.CharField(max_length=2, blank=True, null=True)
    c110 = models.CharField(max_length=2, blank=True, null=True)
    c111 = models.CharField(max_length=2, blank=True, null=True)
    c112 = models.CharField(max_length=2, blank=True, null=True)
    c113 = models.CharField(max_length=2, blank=True, null=True)
    c21 = models.CharField(max_length=2, blank=True, null=True)
    c22 = models.CharField(max_length=2, blank=True, null=True)
    c23 = models.CharField(max_length=2, blank=True, null=True)
    c24 = models.CharField(max_length=2, blank=True, null=True)
    c25 = models.CharField(max_length=2, blank=True, null=True)
    c26 = models.CharField(max_length=2, blank=True, null=True)
    c27 = models.CharField(max_length=2, blank=True, null=True)
    c28 = models.CharField(max_length=2, blank=True, null=True)
    c29 = models.CharField(max_length=2, blank=True, null=True)
    c210 = models.CharField(max_length=2, blank=True, null=True)
    c211 = models.CharField(max_length=2, blank=True, null=True)
    c212 = models.CharField(max_length=2, blank=True, null=True)
    c213 = models.CharField(max_length=2, blank=True, null=True)
    c214 = models.CharField(max_length=2, blank=True, null=True)
    c215 = models.CharField(max_length=2, blank=True, null=True)
    c216 = models.CharField(max_length=2, blank=True, null=True)
    c217 = models.CharField(max_length=2, blank=True, null=True)
    c218 = models.CharField(max_length=2, blank=True, null=True)
    c31 = models.CharField(max_length=2, blank=True, null=True)
    c32 = models.CharField(max_length=2, blank=True, null=True)
    c33 = models.CharField(max_length=2, blank=True, null=True)
    c34 = models.CharField(max_length=2, blank=True, null=True)
    c35 = models.CharField(max_length=2, blank=True, null=True)
    c36 = models.CharField(max_length=2, blank=True, null=True)
    c37 = models.CharField(max_length=2, blank=True, null=True)
    c38 = models.CharField(max_length=2, blank=True, null=True)
    c39 = models.CharField(max_length=2, blank=True, null=True)
    c310 = models.CharField(max_length=2, blank=True, null=True)
    c311 = models.CharField(max_length=2, blank=True, null=True)
    c312 = models.CharField(max_length=2, blank=True, null=True)
    c41 = models.CharField(max_length=2, blank=True, null=True)
    c42 = models.CharField(max_length=2, blank=True, null=True)
    c43 = models.CharField(max_length=2, blank=True, null=True)
    c44 = models.CharField(max_length=2, blank=True, null=True)
    c45 = models.CharField(max_length=2, blank=True, null=True)
    c46 = models.CharField(max_length=2, blank=True, null=True)
    c47 = models.CharField(max_length=2, blank=True, null=True)
    c48 = models.CharField(max_length=2, blank=True, null=True)
    c49 = models.CharField(max_length=2, blank=True, null=True)
    c410 = models.CharField(max_length=2, blank=True, null=True)
    c411 = models.CharField(max_length=2, blank=True, null=True)
    c412 = models.CharField(max_length=2, blank=True, null=True)
    c413 = models.CharField(max_length=2, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cobservaciones = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    cmal = models.CharField(max_length=100, blank=True, null=True)
    cfalta = models.CharField(max_length=100, blank=True, null=True)
    year1 = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'psicologia2'


class Psicologia3(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    c1a = models.CharField(max_length=2, blank=True, null=True)
    c1b = models.CharField(max_length=2, blank=True, null=True)
    c2a = models.CharField(max_length=2, blank=True, null=True)
    c2b = models.CharField(max_length=2, blank=True, null=True)
    c3a = models.CharField(max_length=2, blank=True, null=True)
    c3b = models.CharField(max_length=2, blank=True, null=True)
    c4a = models.CharField(max_length=2, blank=True, null=True)
    c4b = models.CharField(max_length=2, blank=True, null=True)
    c5a = models.CharField(max_length=2, blank=True, null=True)
    c5b = models.CharField(max_length=2, blank=True, null=True)
    c6a = models.CharField(max_length=2, blank=True, null=True)
    c6b = models.CharField(max_length=2, blank=True, null=True)
    c7a = models.CharField(max_length=2, blank=True, null=True)
    c7b = models.CharField(max_length=2, blank=True, null=True)
    c8a = models.CharField(max_length=2, blank=True, null=True)
    c8b = models.CharField(max_length=2, blank=True, null=True)
    c9a = models.CharField(max_length=2, blank=True, null=True)
    c9b = models.CharField(max_length=2, blank=True, null=True)
    c10a = models.CharField(max_length=2, blank=True, null=True)
    c10b = models.CharField(max_length=2, blank=True, null=True)
    c11a = models.CharField(max_length=2, blank=True, null=True)
    c11b = models.CharField(max_length=2, blank=True, null=True)
    c12a = models.CharField(max_length=2, blank=True, null=True)
    c12b = models.CharField(max_length=2, blank=True, null=True)
    c13a = models.CharField(max_length=2, blank=True, null=True)
    c13b = models.CharField(max_length=2, blank=True, null=True)
    c14a = models.CharField(max_length=2, blank=True, null=True)
    c14b = models.CharField(max_length=2, blank=True, null=True)
    c15a = models.CharField(max_length=2, blank=True, null=True)
    c15b = models.CharField(max_length=2, blank=True, null=True)
    c16a = models.CharField(max_length=2, blank=True, null=True)
    c16b = models.CharField(max_length=2, blank=True, null=True)
    c17a = models.CharField(max_length=2, blank=True, null=True)
    c17b = models.CharField(max_length=2, blank=True, null=True)
    c18a = models.CharField(max_length=2, blank=True, null=True)
    c18b = models.CharField(max_length=2, blank=True, null=True)
    c19a = models.CharField(max_length=2, blank=True, null=True)
    c19b = models.CharField(max_length=2, blank=True, null=True)
    c20a = models.CharField(max_length=2, blank=True, null=True)
    c20b = models.CharField(max_length=2, blank=True, null=True)
    c21a = models.CharField(max_length=2, blank=True, null=True)
    c21b = models.CharField(max_length=2, blank=True, null=True)
    c22a = models.CharField(max_length=2, blank=True, null=True)
    c22b = models.CharField(max_length=2, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cobservaciones = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    cmal = models.CharField(max_length=100, blank=True, null=True)
    cfalta = models.CharField(max_length=100, blank=True, null=True)
    year1 = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'psicologia3'


class Psicologia4(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    c11 = models.CharField(max_length=1, blank=True, null=True)
    c12 = models.CharField(max_length=1, blank=True, null=True)
    c13 = models.CharField(max_length=1, blank=True, null=True)
    c14 = models.CharField(max_length=1, blank=True, null=True)
    c15 = models.CharField(max_length=1, blank=True, null=True)
    c16 = models.CharField(max_length=1, blank=True, null=True)
    c17 = models.CharField(max_length=1, blank=True, null=True)
    c18 = models.CharField(max_length=1, blank=True, null=True)
    c19 = models.CharField(max_length=1, blank=True, null=True)
    c110 = models.CharField(max_length=1, blank=True, null=True)
    c21 = models.CharField(max_length=1, blank=True, null=True)
    c22 = models.CharField(max_length=1, blank=True, null=True)
    c23 = models.CharField(max_length=1, blank=True, null=True)
    c24 = models.CharField(max_length=1, blank=True, null=True)
    c25 = models.CharField(max_length=1, blank=True, null=True)
    c26 = models.CharField(max_length=1, blank=True, null=True)
    c31 = models.CharField(max_length=1, blank=True, null=True)
    c32 = models.CharField(max_length=1, blank=True, null=True)
    c33 = models.CharField(max_length=1, blank=True, null=True)
    c34 = models.CharField(max_length=1, blank=True, null=True)
    c35 = models.CharField(max_length=1, blank=True, null=True)
    c36 = models.CharField(max_length=1, blank=True, null=True)
    c37 = models.CharField(max_length=1, blank=True, null=True)
    c38 = models.CharField(max_length=1, blank=True, null=True)
    c41 = models.CharField(max_length=1, blank=True, null=True)
    c42 = models.CharField(max_length=1, blank=True, null=True)
    c43 = models.CharField(max_length=1, blank=True, null=True)
    c44 = models.CharField(max_length=1, blank=True, null=True)
    c45 = models.CharField(max_length=1, blank=True, null=True)
    c46 = models.CharField(max_length=1, blank=True, null=True)
    c47 = models.CharField(max_length=1, blank=True, null=True)
    c51 = models.CharField(max_length=1, blank=True, null=True)
    c52 = models.CharField(max_length=1, blank=True, null=True)
    c53 = models.CharField(max_length=1, blank=True, null=True)
    c54 = models.CharField(max_length=1, blank=True, null=True)
    c55 = models.CharField(max_length=1, blank=True, null=True)
    c56 = models.CharField(max_length=1, blank=True, null=True)
    c57 = models.CharField(max_length=1, blank=True, null=True)
    c61 = models.CharField(max_length=1, blank=True, null=True)
    c62 = models.CharField(max_length=1, blank=True, null=True)
    c63 = models.CharField(max_length=1, blank=True, null=True)
    c64 = models.CharField(max_length=1, blank=True, null=True)
    c65 = models.CharField(max_length=1, blank=True, null=True)
    c66 = models.CharField(max_length=1, blank=True, null=True)
    c67 = models.CharField(max_length=1, blank=True, null=True)
    c68 = models.CharField(max_length=1, blank=True, null=True)
    c69 = models.CharField(max_length=1, blank=True, null=True)
    c71 = models.CharField(max_length=1, blank=True, null=True)
    c72 = models.CharField(max_length=1, blank=True, null=True)
    c73 = models.CharField(max_length=1, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cobservaciones = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    cmal = models.CharField(max_length=100, blank=True, null=True)
    cfalta = models.CharField(max_length=100, blank=True, null=True)
    year1 = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'psicologia4'


class Psicologia5(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    c1 = models.CharField(max_length=1, blank=True, null=True)
    c2 = models.CharField(max_length=1, blank=True, null=True)
    c3 = models.CharField(max_length=1, blank=True, null=True)
    c4 = models.CharField(max_length=1, blank=True, null=True)
    c5 = models.CharField(max_length=1, blank=True, null=True)
    c6 = models.CharField(max_length=1, blank=True, null=True)
    c7 = models.CharField(max_length=1, blank=True, null=True)
    c8 = models.CharField(max_length=1, blank=True, null=True)
    c9 = models.CharField(max_length=1, blank=True, null=True)
    c10 = models.CharField(max_length=1, blank=True, null=True)
    c11 = models.CharField(max_length=1, blank=True, null=True)
    c12 = models.CharField(max_length=1, blank=True, null=True)
    c13 = models.CharField(max_length=1, blank=True, null=True)
    c14 = models.CharField(max_length=1, blank=True, null=True)
    c15 = models.CharField(max_length=1, blank=True, null=True)
    c16 = models.CharField(max_length=1, blank=True, null=True)
    c17 = models.CharField(max_length=1, blank=True, null=True)
    c18 = models.CharField(max_length=1, blank=True, null=True)
    c19 = models.CharField(max_length=1, blank=True, null=True)
    c20 = models.CharField(max_length=1, blank=True, null=True)
    c21 = models.CharField(max_length=1, blank=True, null=True)
    c22 = models.CharField(max_length=1, blank=True, null=True)
    c23 = models.CharField(max_length=1, blank=True, null=True)
    c24 = models.CharField(max_length=1, blank=True, null=True)
    c25 = models.CharField(max_length=1, blank=True, null=True)
    c26 = models.CharField(max_length=1, blank=True, null=True)
    c27 = models.CharField(max_length=1, blank=True, null=True)
    c28 = models.CharField(max_length=1, blank=True, null=True)
    c29 = models.CharField(max_length=1, blank=True, null=True)
    c30 = models.CharField(max_length=1, blank=True, null=True)
    c31 = models.CharField(max_length=1, blank=True, null=True)
    c32 = models.CharField(max_length=1, blank=True, null=True)
    c33 = models.CharField(max_length=1, blank=True, null=True)
    c34 = models.CharField(max_length=1, blank=True, null=True)
    c35 = models.CharField(max_length=1, blank=True, null=True)
    c36 = models.CharField(max_length=1, blank=True, null=True)
    c37 = models.CharField(max_length=1, blank=True, null=True)
    c38 = models.CharField(max_length=1, blank=True, null=True)
    c39 = models.CharField(max_length=1, blank=True, null=True)
    c40 = models.CharField(max_length=1, blank=True, null=True)
    c41 = models.CharField(max_length=1, blank=True, null=True)
    c42 = models.CharField(max_length=1, blank=True, null=True)
    c43 = models.CharField(max_length=1, blank=True, null=True)
    c44 = models.CharField(max_length=1, blank=True, null=True)
    c45 = models.CharField(max_length=1, blank=True, null=True)
    c46 = models.CharField(max_length=1, blank=True, null=True)
    c47 = models.CharField(max_length=1, blank=True, null=True)
    c48 = models.CharField(max_length=1, blank=True, null=True)
    c49 = models.CharField(max_length=1, blank=True, null=True)
    c50 = models.CharField(max_length=1, blank=True, null=True)
    c51 = models.CharField(max_length=1, blank=True, null=True)
    c52 = models.CharField(max_length=1, blank=True, null=True)
    c53 = models.CharField(max_length=1, blank=True, null=True)
    c54 = models.CharField(max_length=1, blank=True, null=True)
    c55 = models.CharField(max_length=1, blank=True, null=True)
    c56 = models.CharField(max_length=1, blank=True, null=True)
    c57 = models.CharField(max_length=1, blank=True, null=True)
    c58 = models.CharField(max_length=1, blank=True, null=True)
    c59 = models.CharField(max_length=1, blank=True, null=True)
    c60 = models.CharField(max_length=1, blank=True, null=True)
    c61 = models.CharField(max_length=1, blank=True, null=True)
    c62 = models.CharField(max_length=1, blank=True, null=True)
    c63 = models.CharField(max_length=1, blank=True, null=True)
    c64 = models.CharField(max_length=1, blank=True, null=True)
    c65 = models.CharField(max_length=1, blank=True, null=True)
    c66 = models.CharField(max_length=1, blank=True, null=True)
    c67 = models.CharField(max_length=1, blank=True, null=True)
    c68 = models.CharField(max_length=1, blank=True, null=True)
    c69 = models.CharField(max_length=1, blank=True, null=True)
    c70 = models.CharField(max_length=1, blank=True, null=True)
    c71 = models.CharField(max_length=1, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cobservaciones = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    cmal = models.CharField(max_length=100, blank=True, null=True)
    cfalta = models.CharField(max_length=100, blank=True, null=True)
    year1 = models.CharField(max_length=4, blank=True, null=True)
    ld = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fd = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    kd = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    hsd = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    dd = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    hid = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    dpd = models.DecimalField(db_column='Dpd', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pad = models.DecimalField(db_column='Pad', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ptd = models.DecimalField(db_column='Ptd', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    esd = models.DecimalField(db_column='Esd', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mad = models.DecimalField(db_column='Mad', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lmm = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fmm = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    kmm = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    hsmm = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    dmm = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    himm = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    dpmm = models.DecimalField(db_column='Dpmm', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pamm = models.DecimalField(db_column='Pamm', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ptmm = models.DecimalField(db_column='Ptmm', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    esmm = models.DecimalField(db_column='Esmm', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mamm = models.DecimalField(db_column='Mamm', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lk = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fk = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    kk = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    hsk = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    dk = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    hik = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    dpk = models.DecimalField(db_column='Dpk', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pak = models.DecimalField(db_column='Pak', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ptk = models.DecimalField(db_column='Ptk', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    esk = models.DecimalField(db_column='Esk', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mak = models.DecimalField(db_column='Mak', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lt = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ft = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    kt = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    hst = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    dt = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    hit = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    dpt = models.DecimalField(db_column='Dpt', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pat = models.DecimalField(db_column='Pat', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ptt = models.DecimalField(db_column='Ptt', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    est = models.DecimalField(db_column='Est', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mat = models.DecimalField(db_column='Mat', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psicologia5'


class Psicologia6(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    c11 = models.CharField(max_length=1, blank=True, null=True)
    c12 = models.CharField(max_length=1, blank=True, null=True)
    c13 = models.CharField(max_length=1, blank=True, null=True)
    c14 = models.CharField(max_length=1, blank=True, null=True)
    c15 = models.CharField(max_length=1, blank=True, null=True)
    c16 = models.CharField(max_length=1, blank=True, null=True)
    c17 = models.CharField(max_length=1, blank=True, null=True)
    c18 = models.CharField(max_length=1, blank=True, null=True)
    c19 = models.CharField(max_length=1, blank=True, null=True)
    c21 = models.CharField(max_length=1, blank=True, null=True)
    c22 = models.CharField(max_length=1, blank=True, null=True)
    c23 = models.CharField(max_length=1, blank=True, null=True)
    c24 = models.CharField(max_length=1, blank=True, null=True)
    c25 = models.CharField(max_length=1, blank=True, null=True)
    c31 = models.CharField(max_length=1, blank=True, null=True)
    c32 = models.CharField(max_length=1, blank=True, null=True)
    c33 = models.CharField(max_length=1, blank=True, null=True)
    c34 = models.CharField(max_length=1, blank=True, null=True)
    c35 = models.CharField(max_length=1, blank=True, null=True)
    c36 = models.CharField(max_length=1, blank=True, null=True)
    c37 = models.CharField(max_length=1, blank=True, null=True)
    c41 = models.CharField(max_length=1, blank=True, null=True)
    c42 = models.CharField(max_length=1, blank=True, null=True)
    c43 = models.CharField(max_length=1, blank=True, null=True)
    c44 = models.CharField(max_length=1, blank=True, null=True)
    c45 = models.CharField(max_length=1, blank=True, null=True)
    c46 = models.CharField(max_length=1, blank=True, null=True)
    c47 = models.CharField(max_length=1, blank=True, null=True)
    c51 = models.CharField(max_length=1, blank=True, null=True)
    c52 = models.CharField(max_length=1, blank=True, null=True)
    c53 = models.CharField(max_length=1, blank=True, null=True)
    c54 = models.CharField(max_length=1, blank=True, null=True)
    c55 = models.CharField(max_length=1, blank=True, null=True)
    c56 = models.CharField(max_length=1, blank=True, null=True)
    c61 = models.CharField(max_length=1, blank=True, null=True)
    c62 = models.CharField(max_length=1, blank=True, null=True)
    c63 = models.CharField(max_length=1, blank=True, null=True)
    c64 = models.CharField(max_length=1, blank=True, null=True)
    c65 = models.CharField(max_length=1, blank=True, null=True)
    c66 = models.CharField(max_length=1, blank=True, null=True)
    c67 = models.CharField(max_length=1, blank=True, null=True)
    c68 = models.CharField(max_length=1, blank=True, null=True)
    c69 = models.CharField(max_length=1, blank=True, null=True)
    c71 = models.CharField(max_length=1, blank=True, null=True)
    c72 = models.CharField(max_length=1, blank=True, null=True)
    c73 = models.CharField(max_length=1, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cobservaciones = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    cmal = models.CharField(max_length=100, blank=True, null=True)
    cfalta = models.CharField(max_length=100, blank=True, null=True)
    c1 = models.CharField(max_length=1, blank=True, null=True)
    c2 = models.CharField(max_length=1, blank=True, null=True)
    c3 = models.CharField(max_length=1, blank=True, null=True)
    c4 = models.CharField(max_length=1, blank=True, null=True)
    c5 = models.CharField(max_length=1, blank=True, null=True)
    c6 = models.CharField(max_length=1, blank=True, null=True)
    c7 = models.CharField(max_length=1, blank=True, null=True)
    c8 = models.CharField(max_length=1, blank=True, null=True)
    c9 = models.CharField(max_length=1, blank=True, null=True)
    c10 = models.CharField(max_length=1, blank=True, null=True)
    year1 = models.CharField(max_length=4, blank=True, null=True)
    c20 = models.CharField(max_length=1, blank=True, null=True)
    c26 = models.CharField(max_length=1, blank=True, null=True)
    c27 = models.CharField(max_length=1, blank=True, null=True)
    c28 = models.CharField(max_length=1, blank=True, null=True)
    c29 = models.CharField(max_length=1, blank=True, null=True)
    c30 = models.CharField(max_length=1, blank=True, null=True)
    c38 = models.CharField(max_length=1, blank=True, null=True)
    c39 = models.CharField(max_length=1, blank=True, null=True)
    c40 = models.CharField(max_length=1, blank=True, null=True)
    c48 = models.CharField(max_length=1, blank=True, null=True)
    c49 = models.CharField(max_length=1, blank=True, null=True)
    c50 = models.CharField(max_length=1, blank=True, null=True)
    c57 = models.CharField(max_length=1, blank=True, null=True)
    c58 = models.CharField(max_length=1, blank=True, null=True)
    c59 = models.CharField(max_length=1, blank=True, null=True)
    c60 = models.CharField(max_length=1, blank=True, null=True)
    c70 = models.CharField(max_length=1, blank=True, null=True)
    cdiagnostico3 = models.TextField(blank=True, null=True)
    cdiagnostico4 = models.TextField(blank=True, null=True)
    cdiagnostico5 = models.TextField(blank=True, null=True)
    cdiagnostico2 = models.TextField(blank=True, null=True)
    cdiagnostico6 = models.TextField(blank=True, null=True)
    cdiagnostico7 = models.TextField(blank=True, null=True)
    cdiagnostico1 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'psicologia6'


class Psicologia7(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    c1 = models.CharField(max_length=1, blank=True, null=True)
    c2 = models.CharField(max_length=1, blank=True, null=True)
    c3 = models.CharField(max_length=1, blank=True, null=True)
    c4 = models.CharField(max_length=1, blank=True, null=True)
    c5 = models.CharField(max_length=1, blank=True, null=True)
    c6 = models.CharField(max_length=1, blank=True, null=True)
    c7 = models.CharField(max_length=1, blank=True, null=True)
    c8 = models.CharField(max_length=1, blank=True, null=True)
    c9 = models.CharField(max_length=1, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cobservaciones = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    cmal = models.CharField(max_length=100, blank=True, null=True)
    cfalta = models.CharField(max_length=100, blank=True, null=True)
    year1 = models.CharField(max_length=4, blank=True, null=True)
    cn1 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cn2 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cn3 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cn4 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cn5 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cn6 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cn7 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cn8 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cn9 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nfinal = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'psicologia7'


class Psicologia8(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    c1 = models.CharField(max_length=1000, blank=True, null=True)
    c2 = models.CharField(max_length=1000, blank=True, null=True)
    c3 = models.CharField(max_length=1000, blank=True, null=True)
    c4 = models.CharField(max_length=1000, blank=True, null=True)
    c5 = models.CharField(max_length=1000, blank=True, null=True)
    c6 = models.CharField(max_length=1000, blank=True, null=True)
    c7 = models.CharField(max_length=1000, blank=True, null=True)
    c8 = models.CharField(max_length=1000, blank=True, null=True)
    c9 = models.CharField(max_length=1000, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    year1 = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'psicologia8'


class Psicologia9(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    c1 = models.CharField(max_length=1, blank=True, null=True)
    c2 = models.CharField(max_length=1, blank=True, null=True)
    c3 = models.CharField(max_length=1, blank=True, null=True)
    c4 = models.CharField(max_length=1, blank=True, null=True)
    c5 = models.CharField(max_length=1, blank=True, null=True)
    c6 = models.CharField(max_length=1, blank=True, null=True)
    c7 = models.CharField(max_length=1, blank=True, null=True)
    c8 = models.CharField(max_length=1, blank=True, null=True)
    c9 = models.CharField(max_length=1, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    year1 = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'psicologia9'


class Psicologico(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    cconclusion = models.CharField(max_length=100, blank=True, null=True)
    cestado1 = models.CharField(max_length=2, blank=True, null=True)
    personalidad = models.CharField(max_length=10, blank=True, null=True)
    inteligencia = models.CharField(max_length=10, blank=True, null=True)
    agora = models.CharField(max_length=100, blank=True, null=True)
    visomo = models.CharField(max_length=100, blank=True, null=True)
    psicopa = models.CharField(max_length=100, blank=True, null=True)
    orga = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'psicologico'


class Psicotecnico(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    cconclusion = models.CharField(max_length=100, blank=True, null=True)
    cestado1 = models.CharField(max_length=2, blank=True, null=True)
    cvisiometria = models.CharField(max_length=10, blank=True, null=True)
    cpalanca = models.CharField(max_length=10, blank=True, null=True)
    cpunteado = models.CharField(max_length=10, blank=True, null=True)
    creactimetro = models.CharField(max_length=10, blank=True, null=True)
    cagudezaod = models.CharField(max_length=6, blank=True, null=True)
    cagudezaoi = models.CharField(max_length=6, blank=True, null=True)
    caguconclu = models.CharField(max_length=8, blank=True, null=True)
    crecoconclu = models.CharField(max_length=8, blank=True, null=True)
    ccolconclu = models.CharField(max_length=8, blank=True, null=True)
    cfollconclu = models.CharField(max_length=8, blank=True, null=True)
    cfolvconclu = models.CharField(max_length=8, blank=True, null=True)
    cestconclu = models.CharField(max_length=8, blank=True, null=True)
    cvisconclu = models.CharField(max_length=8, blank=True, null=True)
    cencconclu = models.CharField(max_length=8, blank=True, null=True)
    crecencconclu = models.CharField(max_length=8, blank=True, null=True)
    ccamconclu = models.CharField(max_length=8, blank=True, null=True)
    creactimetropro = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cpunteadotie = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cpunteadoper = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cpunteadoerro = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cpalancat = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cpalancaerr = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cpalancatiempo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cestonclu = models.CharField(max_length=8, blank=True, null=True)
    cequipos1 = models.CharField(max_length=3, blank=True, null=True)
    cequipos2 = models.CharField(max_length=3, blank=True, null=True)
    cequipos3 = models.CharField(max_length=3, blank=True, null=True)
    idcalibracion = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ctipo = models.CharField(max_length=1, blank=True, null=True)
    ctipo1 = models.CharField(max_length=1, blank=True, null=True)
    ctipo2 = models.CharField(max_length=1, blank=True, null=True)
    cconductor = models.CharField(max_length=1, blank=True, null=True)
    cconductor1 = models.CharField(max_length=1, blank=True, null=True)
    esfuerzo = models.CharField(max_length=200, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cestere = models.CharField(max_length=2, blank=True, null=True)
    cagudezaodcerca = models.CharField(max_length=8, blank=True, null=True)
    cagudezaoicerca = models.CharField(max_length=8, blank=True, null=True)
    creconocimiento = models.CharField(max_length=8, blank=True, null=True)
    ccolores = models.CharField(max_length=8, blank=True, null=True)
    cfolialateral = models.CharField(max_length=8, blank=True, null=True)
    cfoliavertical = models.CharField(max_length=8, blank=True, null=True)
    cestereopsis = models.CharField(max_length=8, blank=True, null=True)
    cvisionnocturna = models.CharField(max_length=8, blank=True, null=True)
    cencandilamiento = models.CharField(max_length=8, blank=True, null=True)
    crecuperacion = models.CharField(max_length=8, blank=True, null=True)
    ccampovisual = models.CharField(max_length=8, blank=True, null=True)
    esfuerzoapro = models.CharField(max_length=1, blank=True, null=True)
    esfuerzodes = models.CharField(max_length=1, blank=True, null=True)
    esfuerzono = models.CharField(max_length=1, blank=True, null=True)
    anti = models.CharField(max_length=50, blank=True, null=True)
    anticonclu = models.CharField(max_length=100, blank=True, null=True)
    corbi = models.CharField(max_length=100, blank=True, null=True)
    corbiconclu = models.CharField(max_length=100, blank=True, null=True)
    monot = models.CharField(max_length=100, blank=True, null=True)
    monotconclu = models.CharField(max_length=100, blank=True, null=True)
    reac = models.CharField(max_length=100, blank=True, null=True)
    reacconclu = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'psicotecnico'


class PsicotecnicoIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cconclusion = models.CharField(max_length=100, blank=True, null=True)
    cestado1 = models.CharField(max_length=2, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'psicotecnico_iud'


class Psicottab(models.Model):
    ccodtab = models.CharField(max_length=3, blank=True, null=True)
    ccodigo = models.CharField(max_length=2, blank=True, null=True)
    cdescri = models.TextField(blank=True, null=True)
    ctipo = models.CharField(max_length=5, blank=True, null=True)
    ccalculo = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'psicottab'


class Ptecsup(models.Model):
    chistoria = models.CharField(max_length=15, blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    idocu = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    aptitud = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ptecsup'


class Rayosx(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    ctipo = models.CharField(max_length=3, blank=True, null=True)
    cdiagnostico = models.CharField(max_length=30, blank=True, null=True)
    ccalidad = models.CharField(max_length=3, blank=True, null=True)
    ccausas = models.CharField(max_length=3, blank=True, null=True)
    ccomentario = models.TextField(blank=True, null=True)
    c21supder = models.CharField(max_length=1, blank=True, null=True)
    c21supizq = models.CharField(max_length=1, blank=True, null=True)
    c21medizq = models.CharField(max_length=1, blank=True, null=True)
    c21medder = models.CharField(max_length=1, blank=True, null=True)
    c21infizq = models.CharField(max_length=1, blank=True, null=True)
    c21infder = models.CharField(max_length=1, blank=True, null=True)
    c22 = models.CharField(max_length=3, blank=True, null=True)
    c23prip = models.CharField(max_length=1, blank=True, null=True)
    c23priq = models.CharField(max_length=1, blank=True, null=True)
    c23prir = models.CharField(max_length=1, blank=True, null=True)
    c23pris = models.CharField(max_length=1, blank=True, null=True)
    c23prit = models.CharField(max_length=1, blank=True, null=True)
    c23priu = models.CharField(max_length=1, blank=True, null=True)
    c23secp = models.CharField(max_length=1, blank=True, null=True)
    c23secq = models.CharField(max_length=1, blank=True, null=True)
    c23secr = models.CharField(max_length=1, blank=True, null=True)
    c23secs = models.CharField(max_length=1, blank=True, null=True)
    c23sect = models.CharField(max_length=1, blank=True, null=True)
    c23secu = models.CharField(max_length=1, blank=True, null=True)
    c24 = models.CharField(max_length=3, blank=True, null=True)
    canorpleu = models.CharField(max_length=1, blank=True, null=True)
    c31sitiopared = models.CharField(max_length=3, blank=True, null=True)
    c31sitiofrente = models.CharField(max_length=3, blank=True, null=True)
    c31sitiodiafr = models.CharField(max_length=3, blank=True, null=True)
    c31sitiootro = models.CharField(max_length=3, blank=True, null=True)
    c31calcipared = models.CharField(max_length=3, blank=True, null=True)
    c31calcifrente = models.CharField(max_length=3, blank=True, null=True)
    c31calcidiafr = models.CharField(max_length=3, blank=True, null=True)
    c31calciotro = models.CharField(max_length=3, blank=True, null=True)
    c31oblite = models.CharField(max_length=3, blank=True, null=True)
    c32paredperfil = models.CharField(max_length=3, blank=True, null=True)
    c32paredfrente = models.CharField(max_length=3, blank=True, null=True)
    c32calciperfil = models.CharField(max_length=3, blank=True, null=True)
    c32calcifrente = models.CharField(max_length=3, blank=True, null=True)
    c32exten21 = models.CharField(max_length=3, blank=True, null=True)
    c32ancho21 = models.CharField(max_length=3, blank=True, null=True)
    csimbolo = models.TextField(blank=True, null=True)
    csimb = models.CharField(max_length=1, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    c31exten11 = models.CharField(max_length=3, blank=True, null=True)
    c31ancho11 = models.CharField(max_length=3, blank=True, null=True)
    c31ancho1 = models.CharField(max_length=3, blank=True, null=True)
    c31exten1 = models.CharField(max_length=3, blank=True, null=True)
    c32exten22 = models.CharField(max_length=3, blank=True, null=True)
    c32ancho2 = models.CharField(max_length=3, blank=True, null=True)
    cvertice = models.CharField(max_length=100, blank=True, null=True)
    ccampos = models.CharField(max_length=100, blank=True, null=True)
    chilos = models.CharField(max_length=100, blank=True, null=True)
    csenos = models.CharField(max_length=100, blank=True, null=True)
    cmediastinos = models.CharField(max_length=100, blank=True, null=True)
    csilueta = models.CharField(max_length=100, blank=True, null=True)
    cotros = models.CharField(max_length=200, blank=True, null=True)
    csin = models.CharField(max_length=1, blank=True, null=True)
    cexpo = models.CharField(max_length=1, blank=True, null=True)
    cconclurad = models.CharField(max_length=400, blank=True, null=True)
    cdianeou = models.CharField(max_length=200, blank=True, null=True)
    cdiagnosticosf = models.CharField(max_length=50, blank=True, null=True)
    nsin = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nexpo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cflagestado = models.CharField(max_length=1, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=100, blank=True, null=True)
    cdiagnos = models.CharField(max_length=2, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    crayos = models.IntegerField(blank=True, null=True)
    cmedico = models.IntegerField(blank=True, null=True)
    idcalibracion = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rayosx'


class RayosxIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    ccomentario = models.TextField(blank=True, null=True)
    cconclurad = models.CharField(max_length=400, blank=True, null=True)
    cdiagnosticosf = models.CharField(max_length=50, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rayosx_iud'


class Reevaluaciones(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    captitud = models.CharField(max_length=20, blank=True, null=True)
    cmedico = models.CharField(max_length=100, blank=True, null=True)
    cobservacion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reevaluaciones'


class Regional(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    ccuello = models.TextField(blank=True, null=True)
    cnariz = models.TextField(blank=True, null=True)
    cboca = models.TextField(blank=True, null=True)
    ctorax = models.TextField(blank=True, null=True)
    ccorazon = models.TextField(blank=True, null=True)
    cpulso = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cpresis = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cpredias = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    crespi = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    csatura = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cpulmones = models.TextField(blank=True, null=True)
    cmiembrosup = models.TextField(blank=True, null=True)
    cmiembroinf = models.TextField(blank=True, null=True)
    creflejos = models.TextField(blank=True, null=True)
    ccolumnave = models.TextField(blank=True, null=True)
    cabdomen = models.TextField(blank=True, null=True)
    ctactorec = models.CharField(max_length=3, blank=True, null=True)
    canillos = models.TextField(blank=True, null=True)
    chernia = models.TextField(blank=True, null=True)
    cvarices = models.TextField(blank=True, null=True)
    corggeni = models.TextField(blank=True, null=True)
    cganglios = models.TextField(blank=True, null=True)
    clenguaje = models.TextField(blank=True, null=True)
    cdiagnostico = models.CharField(max_length=100, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    cequili = models.TextField(blank=True, null=True)
    cneuro = models.TextField(blank=True, null=True)
    ccara = models.TextField(blank=True, null=True)
    cpiel = models.TextField(blank=True, null=True)
    ccabello = models.TextField(blank=True, null=True)
    ccie10 = models.CharField(max_length=20, blank=True, null=True)
    cfur = models.CharField(max_length=12, blank=True, null=True)
    crcirre = models.CharField(max_length=1, blank=True, null=True)
    crcregu = models.CharField(max_length=1, blank=True, null=True)
    crcdias = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    crctiem = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    cirs = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    cmac = models.CharField(max_length=20, blank=True, null=True)
    cmamas = models.CharField(max_length=100, blank=True, null=True)
    cprusup = models.CharField(max_length=2, blank=True, null=True)
    cprumed = models.CharField(max_length=2, blank=True, null=True)
    cppld = models.CharField(max_length=2, blank=True, null=True)
    cppli = models.CharField(max_length=2, blank=True, null=True)
    cmarcha = models.TextField(blank=True, null=True)
    cfuermus = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regional'


class RegionalIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.CharField(max_length=100, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regional_iud'


class Reporte(models.Model):
    id = models.AutoField(primary_key=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    dato = models.CharField(max_length=40, blank=True, null=True)
    idpersonal = models.CharField(max_length=5, blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reporte'


class Reporteador(models.Model):
    tfecha = models.DateTimeField(blank=True, null=True)
    thora = models.TimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    cselect = models.TextField(blank=True, null=True)
    cnombre = models.CharField(max_length=50, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'reporteador'


class RolesGrupoUsuario(models.Model):
    id_grupo = models.IntegerField(blank=True, null=True)
    id_form = models.IntegerField(blank=True, null=True)
    acceso = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    impresion = models.CharField(max_length=1, blank=True, null=True)
    eliminar = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles_grupo_usuario'


class Rutas(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    cons3 = models.CharField(max_length=2, blank=True, null=True)
    cons4 = models.CharField(max_length=2, blank=True, null=True)
    cons5 = models.CharField(max_length=2, blank=True, null=True)
    cons1 = models.CharField(max_length=2, blank=True, null=True)
    cons6 = models.CharField(max_length=2, blank=True, null=True)
    cons7 = models.CharField(max_length=2, blank=True, null=True)
    cons8 = models.CharField(max_length=2, blank=True, null=True)
    cons9 = models.CharField(max_length=2, blank=True, null=True)
    cons10 = models.CharField(max_length=2, blank=True, null=True)
    cons11 = models.CharField(max_length=2, blank=True, null=True)
    cons2 = models.CharField(max_length=2, blank=True, null=True)
    dfecha = models.DateField(blank=True, null=True)
    lcons1 = models.CharField(max_length=1, blank=True, null=True)
    lcons2 = models.CharField(max_length=1, blank=True, null=True)
    lcons3 = models.CharField(max_length=1, blank=True, null=True)
    lcons4 = models.CharField(max_length=1, blank=True, null=True)
    lcons5 = models.CharField(max_length=1, blank=True, null=True)
    lcons6 = models.CharField(max_length=1, blank=True, null=True)
    lcons7 = models.CharField(max_length=1, blank=True, null=True)
    lcons8 = models.CharField(max_length=1, blank=True, null=True)
    lcons9 = models.CharField(max_length=1, blank=True, null=True)
    lcons10 = models.CharField(max_length=1, blank=True, null=True)
    lcons11 = models.CharField(max_length=1, blank=True, null=True)
    cons12 = models.CharField(max_length=2, blank=True, null=True)
    lcons12 = models.CharField(max_length=1, blank=True, null=True)
    cons13 = models.CharField(max_length=2, blank=True, null=True)
    lcons13 = models.CharField(max_length=1, blank=True, null=True)
    cons14 = models.CharField(max_length=2, blank=True, null=True)
    lcon14 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rutas'


class Sucursal(models.Model):
    cnombre = models.CharField(max_length=100)
    cdomicilio = models.TextField(blank=True, null=True)
    ctelefono = models.CharField(max_length=9, blank=True, null=True)
    ccontacto = models.CharField(max_length=100, blank=True, null=True)
    cemail = models.TextField(blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursal'


class Systtab(models.Model):
    ccodtab = models.CharField(max_length=3, blank=True, null=True)
    ccodigo = models.CharField(max_length=2, blank=True, null=True)
    cdescri = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'systtab'


class Tabcargo(models.Model):
    id = models.DecimalField(max_digits=2, decimal_places=2, primary_key=True)
    nombre = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tabcargo'


class Tabdetcargo(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    nombre = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tabdetcargo'


class Tomalab(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    cconclusion = models.CharField(max_length=100, blank=True, null=True)
    cestado1 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tomalab'


class TomalabIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cconclusion = models.CharField(max_length=100, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tomalab_iud'


class Tomarayosx(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    cconclusion = models.CharField(max_length=20000, blank=True, null=True)
    cestado1 = models.CharField(max_length=2, blank=True, null=True)
    cfinal = models.CharField(max_length=20, blank=True, null=True)
    cfinal2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tomarayosx'


class Tomarayosx1(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    cconclusion = models.CharField(max_length=20000, blank=True, null=True)
    cestado1 = models.CharField(max_length=2, blank=True, null=True)
    cfinal = models.CharField(max_length=20, blank=True, null=True)
    cfinal2 = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tomarayosx1'


class Tomarayosx1Iud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cconclusion = models.CharField(max_length=20000, blank=True, null=True)
    cestado1 = models.CharField(max_length=2, blank=True, null=True)
    cfinal = models.CharField(max_length=20, blank=True, null=True)
    cfinal2 = models.CharField(max_length=100, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tomarayosx1_iud'


class TomarayosxIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cconclusion = models.CharField(max_length=20000, blank=True, null=True)
    cestado1 = models.CharField(max_length=2, blank=True, null=True)
    cfinal = models.CharField(max_length=20, blank=True, null=True)
    cfinal2 = models.CharField(max_length=100, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tomarayosx_iud'


class Tratantes(models.Model):
    cdni = models.CharField(max_length=8, blank=True, null=True)
    cnombre = models.CharField(max_length=100, blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cdiagnostico = models.TextField(blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    capto = models.CharField(max_length=10, blank=True, null=True)
    cobservacion = models.TextField(blank=True, null=True)
    crecomendacion = models.TextField(blank=True, null=True)
    capellidos = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tratantes'


class Triaje(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    npulso = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    nfrecres = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ntemperatura = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    npeso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ntalla = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    cobservacion = models.TextField(blank=True, null=True)
    cspo2 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    npresion = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    npresion2 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cinsmax = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cespfor = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ccintura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ccadera = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    year1 = models.CharField(max_length=4, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    idcalibracionbalanza = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    idcalibracionmonitor = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'triaje'


class TriajeIud(models.Model):
    idop = models.CharField(max_length=1)
    idchistoria = models.CharField(max_length=16, blank=True, null=True)
    idsimon = models.IntegerField(blank=True, null=True)
    chistoria = models.CharField(max_length=11, blank=True, null=True)
    cobservacion = models.TextField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    ccerrado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    fechaop = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'triaje_iud'


class Ubigeo(models.Model):
    ccoddpto = models.CharField(max_length=2, blank=True, null=True)
    ccodprov = models.CharField(max_length=2, blank=True, null=True)
    ccoddist = models.CharField(max_length=2, blank=True, null=True)
    cdesdpto = models.TextField(blank=True, null=True)
    cdesprov = models.TextField(blank=True, null=True)
    cdesdist = models.TextField(blank=True, null=True)
    ccodubi = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ubigeo'


class Userlogin(models.Model):
    cuserlogin = models.CharField(max_length=10, blank=True, null=True)
    cpassword = models.CharField(max_length=20, blank=True, null=True)
    cruc = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userlogin'


class Usuarios(models.Model):
    usuario = models.CharField(max_length=20)
    clave = models.CharField(max_length=22)
    cempresa = models.CharField(max_length=11, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'


class ValidacionPersona(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria')
    tfecha = models.DateTimeField(blank=True, null=True)
    temphuella = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'validacion_persona'


class Visualizacion(models.Model):
    chistoria = models.ForeignKey(Clientes, db_column='chistoria', blank=True, null=True)
    tfecha = models.DateTimeField(blank=True, null=True)
    nsecuencia = models.IntegerField(blank=True, null=True)
    cusuario = models.CharField(max_length=5, blank=True, null=True)
    cestado = models.CharField(max_length=1, blank=True, null=True)
    csucursal = models.CharField(max_length=2, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    cirrobs = models.CharField(max_length=100, blank=True, null=True)
    cirr = models.CharField(max_length=1, blank=True, null=True)
    cpesobs = models.CharField(max_length=100, blank=True, null=True)
    cpes = models.CharField(max_length=1, blank=True, null=True)
    ccefobs = models.CharField(max_length=100, blank=True, null=True)
    ccef = models.CharField(max_length=1, blank=True, null=True)
    cpinobs = models.CharField(max_length=100, blank=True, null=True)
    cpin = models.CharField(max_length=1, blank=True, null=True)
    cdolobs = models.CharField(max_length=100, blank=True, null=True)
    cdol = models.CharField(max_length=1, blank=True, null=True)
    cdesobs = models.CharField(max_length=100, blank=True, null=True)
    cdes = models.CharField(max_length=1, blank=True, null=True)
    cdolojoobs = models.CharField(max_length=100, blank=True, null=True)
    cdolojo = models.CharField(max_length=1, blank=True, null=True)
    cqueobs = models.CharField(max_length=100, blank=True, null=True)
    cque = models.CharField(max_length=1, blank=True, null=True)
    cdolsieobs = models.CharField(max_length=100, blank=True, null=True)
    cdolsie = models.CharField(max_length=1, blank=True, null=True)
    cdolparobs = models.CharField(max_length=100, blank=True, null=True)
    cdolpar = models.CharField(max_length=1, blank=True, null=True)
    clagobs = models.CharField(max_length=100, blank=True, null=True)
    clag = models.CharField(max_length=1, blank=True, null=True)
    cseqobs = models.CharField(max_length=100, blank=True, null=True)
    cseq = models.CharField(max_length=1, blank=True, null=True)
    cticobs = models.CharField(max_length=100, blank=True, null=True)
    ctic = models.CharField(max_length=1, blank=True, null=True)
    cvisobs = models.CharField(max_length=100, blank=True, null=True)
    cvis = models.CharField(max_length=1, blank=True, null=True)
    cimadobobs = models.CharField(max_length=100, blank=True, null=True)
    cimadob = models.CharField(max_length=1, blank=True, null=True)
    cmanobs = models.CharField(max_length=100, blank=True, null=True)
    cman = models.CharField(max_length=1, blank=True, null=True)
    cverobs = models.CharField(max_length=100, blank=True, null=True)
    cver = models.CharField(max_length=1, blank=True, null=True)
    cultobs = models.CharField(max_length=100, blank=True, null=True)
    cult = models.CharField(max_length=1, blank=True, null=True)
    cultmej = models.CharField(max_length=1, blank=True, null=True)
    culthaemp = models.CharField(max_length=1, blank=True, null=True)
    cultigual = models.CharField(max_length=1, blank=True, null=True)
    cparalejosobs = models.CharField(max_length=100, blank=True, null=True)
    cparalejos = models.CharField(max_length=1, blank=True, null=True)
    cparacercasobs = models.CharField(max_length=100, blank=True, null=True)
    cparacerca = models.CharField(max_length=1, blank=True, null=True)
    cbifocalesobs = models.CharField(max_length=100, blank=True, null=True)
    cbifocales = models.CharField(max_length=1, blank=True, null=True)
    ctrifocalesobs = models.CharField(max_length=100, blank=True, null=True)
    ctrifocales = models.CharField(max_length=1, blank=True, null=True)
    cprogresivasobs = models.CharField(max_length=100, blank=True, null=True)
    cprogresivas = models.CharField(max_length=1, blank=True, null=True)
    clentesobs = models.CharField(max_length=100, blank=True, null=True)
    clentes = models.CharField(max_length=1, blank=True, null=True)
    canolente = models.CharField(max_length=100, blank=True, null=True)
    canograducacion = models.CharField(max_length=100, blank=True, null=True)
    cadapbuena = models.CharField(max_length=1, blank=True, null=True)
    cadapregular = models.CharField(max_length=1, blank=True, null=True)
    cadapmala = models.CharField(max_length=1, blank=True, null=True)
    cdolorsobs = models.CharField(max_length=100, blank=True, null=True)
    cdolor = models.CharField(max_length=1, blank=True, null=True)
    cdolcuelloobs = models.CharField(max_length=100, blank=True, null=True)
    cdolcuello = models.CharField(max_length=1, blank=True, null=True)
    cdolespaldasobs = models.CharField(max_length=100, blank=True, null=True)
    cdolespalda = models.CharField(max_length=1, blank=True, null=True)
    cdolrinonesobs = models.CharField(max_length=100, blank=True, null=True)
    cdolrinones = models.CharField(max_length=1, blank=True, null=True)
    cdolbrazosobs = models.CharField(max_length=100, blank=True, null=True)
    cdolbrazos = models.CharField(max_length=1, blank=True, null=True)
    cdolmanosobs = models.CharField(max_length=100, blank=True, null=True)
    cdolmanos = models.CharField(max_length=1, blank=True, null=True)
    cdolpiernasobs = models.CharField(max_length=100, blank=True, null=True)
    cdolpiernas = models.CharField(max_length=1, blank=True, null=True)
    ccalambresobs = models.CharField(max_length=100, blank=True, null=True)
    ccalambres = models.CharField(max_length=1, blank=True, null=True)
    cperfueobs = models.CharField(max_length=100, blank=True, null=True)
    cperfue = models.CharField(max_length=1, blank=True, null=True)
    cdolartobs = models.CharField(max_length=100, blank=True, null=True)
    cdolart = models.CharField(max_length=1, blank=True, null=True)
    ccruartobs = models.CharField(max_length=100, blank=True, null=True)
    ccruart = models.CharField(max_length=1, blank=True, null=True)
    ccansancioobs = models.CharField(max_length=100, blank=True, null=True)
    ccansancio = models.CharField(max_length=1, blank=True, null=True)
    ccanlevaobs = models.CharField(max_length=100, blank=True, null=True)
    ccanlev = models.CharField(max_length=1, blank=True, null=True)
    ccantrabobs = models.CharField(max_length=100, blank=True, null=True)
    ccantrab = models.CharField(max_length=1, blank=True, null=True)
    ccanterobs = models.CharField(max_length=100, blank=True, null=True)
    ccanter = models.CharField(max_length=1, blank=True, null=True)
    cdifdorobs = models.CharField(max_length=100, blank=True, null=True)
    cdifdor = models.CharField(max_length=1, blank=True, null=True)
    cdifconobs = models.CharField(max_length=100, blank=True, null=True)
    cdifcon = models.CharField(max_length=1, blank=True, null=True)
    cpalpiobs = models.CharField(max_length=100, blank=True, null=True)
    cpalpi = models.CharField(max_length=1, blank=True, null=True)
    ctembloobs = models.CharField(max_length=100, blank=True, null=True)
    ctemblo = models.CharField(max_length=1, blank=True, null=True)
    ctrandigobs = models.CharField(max_length=100, blank=True, null=True)
    ctrandig = models.CharField(max_length=1, blank=True, null=True)
    cnervioobs = models.CharField(max_length=100, blank=True, null=True)
    cnervio = models.CharField(max_length=1, blank=True, null=True)
    cansiedadobs = models.CharField(max_length=100, blank=True, null=True)
    cansiedad = models.CharField(max_length=1, blank=True, null=True)
    cangustiaobs = models.CharField(max_length=100, blank=True, null=True)
    cangustia = models.CharField(max_length=1, blank=True, null=True)
    cirritabilidadobs = models.CharField(max_length=100, blank=True, null=True)
    cirritabilidad = models.CharField(max_length=1, blank=True, null=True)
    cagotamientoobs = models.CharField(max_length=100, blank=True, null=True)
    cagotamiento = models.CharField(max_length=1, blank=True, null=True)
    cpesimismoobs = models.CharField(max_length=100, blank=True, null=True)
    cpesimismo = models.CharField(max_length=1, blank=True, null=True)
    cdepresionobs = models.CharField(max_length=100, blank=True, null=True)
    cdepresion = models.CharField(max_length=1, blank=True, null=True)
    cfrustacionobs = models.CharField(max_length=100, blank=True, null=True)
    cfrustacion = models.CharField(max_length=1, blank=True, null=True)
    cfrustacionlabobs = models.CharField(max_length=100, blank=True, null=True)
    cfrustacionlab = models.CharField(max_length=1, blank=True, null=True)
    cfrustacionsocobs = models.CharField(max_length=100, blank=True, null=True)
    cfrustacionsoc = models.CharField(max_length=1, blank=True, null=True)
    cfrustacionperobs = models.CharField(max_length=100, blank=True, null=True)
    cfrustacionper = models.CharField(max_length=1, blank=True, null=True)
    cdiagnostico = models.CharField(max_length=100, blank=True, null=True)
    crecomendaciones = models.CharField(max_length=200, blank=True, null=True)
    ccie10 = models.CharField(max_length=20, blank=True, null=True)
    cambas = models.CharField(max_length=1, blank=True, null=True)
    cambasobs = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visualizacion'
