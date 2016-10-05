from django import forms
from .models import Weather, Town , Clientes ,Triaje


class WeatherForm(forms.ModelForm):
    town = forms.ModelChoiceField(
        queryset=Town.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Weather
        fields = ['town']
        
class TriajeForm(forms.ModelForm):
    town = forms.ModelChoiceField(
        queryset=Triaje.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Triaje
        fields = ['chistoria']

class ClientesForm(forms.ModelForm):
    town = forms.ModelChoiceField(
        queryset=Clientes.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Clientes
        fields = ['chistoria']
