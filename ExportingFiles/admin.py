from django.contrib import admin
from .models import Town, Weather, Clientes, Triaje


class TownAdmin(admin.ModelAdmin):
    list_display = ('name', 'county')
    ordering = ['county', 'name']


class WeatherAdmin(admin.ModelAdmin):
    list_display = ('town', 'date')
    ordering = ['town', 'date']
class ClientesAdmin(admin.ModelAdmin):
	list_display = ('chistoria','tfecha')
	ordering = ['tfecha','chistoria']

class TriajeAdmin(admin.ModelAdmin):
	list_display = ('chistoria','tfecha')
	ordering = ['tfecha','chistoria']	

admin.site.register(Town, TownAdmin)
admin.site.register(Weather, WeatherAdmin)
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Triaje, TriajeAdmin)
