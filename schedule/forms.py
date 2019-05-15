from django import forms
from .models import ClassEnrolled, Groups, TallerGuitarra, Observador, Inter
from django.utils.translation import ugettext_lazy as _

class InterForm(forms.ModelForm):
    class Meta:
        model = Inter
        fields = ('week1_12', 'week1_13', 'week2_12', 'week2_13',)
        exclude = ('id_enrolled',)
        labels = {
            'week1_12': _('12:00 - 13:30'),
            'week1_13': _('13:35 - 15:05'),
            'week2_12': _('12:00 - 13:30'),
            'week2_13': _('13:35 - 15:05'),
        }

class TallerGuitarraForm(forms.ModelForm):
    class Meta:
        model = TallerGuitarra
        fields = ('id_class',)
        exclude = ('id_enrolled',)
        labels = {
            'id_class': _('Taller'),
        }


class ObservadoresForm(forms.ModelForm):
    class Meta:
        model = Observador
        fields = ('id_class',)
        exclude = ('id_enrolled',)
        labels = {
            'id_class': _('Fechas'),
        }


class ClassEnrolledForm(forms.ModelForm):
    class Meta:
        model = ClassEnrolled
        fields = ('id_program', 'id_level', 'id_class')
        exclude = ('id_enrolled}',)
        labels ={
            'id_program': _('Programa'),
            'id_level': _('Nivel'),
            'id_class': _('Clase'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class RegisterGroup(forms.ModelForm):
    class Meta:
        model = Groups
        fields=()