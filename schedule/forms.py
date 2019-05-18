from django import forms
from .models import ClassEnrolled, Groups, TallerGuitarra, Observador, Inter, Intensivo, Elemental, Independiente
from django.utils.translation import ugettext_lazy as _

class IndependienteForm(forms.ModelForm):
    class Meta:
        model = Independiente
        fields = ('p9', 'p10', 'p3', 'p5', 's9', 's10', 's3', 's5')
        exclude = ('id_enrolled', 'weeks', 'classes')
        labels = {
            'p9': _('9:00 am - 10:30 am'),
            'p10': _('10:35 am - 12:05 pm'),
            'p3': _('3:30 pm - 5:00 pm'),
            'p5': _('5:05 pm - 6:35 pm'),
            's9': _('9:00 am - 10:30 am'),
            's10': _('10:35 am - 12:05 pm'),
            's3': _('3:30 pm - 5:00 pm'),
            's5': _('5:05 pm - 6:35 pm'),
        }


class ElementalForm(forms.ModelForm):
    class Meta:
        model = Elemental
        fields = ('n1', 'n2', 'j1', 'j2',)
        exclude = ('id_enrolled', 'level', 'weeks')
        labels = {
            'n1': _('10:35 am - 12:05 pm'),
            'n2': _('10:35 am - 12:05 pm'),
            'j1': _('9:00 am - 12:05 pm'),
            'j2': _('9:00 am - 12:05 pm'),
        }

class IntensivoForm(forms.ModelForm):
    class Meta:
        model = Intensivo
        fields = ('n1m1', 'n1m2', 'n2m1', 'n2m2',
                  'b1m1', 'b1m2', 'b2m1', 'b2m2',
                  'i1m1', 'i1m2', 'i1v1', 'i1v2', 'i2m1', 'i2m2', 'i2v1', 'i2v2',
                  'a1m1', 'a1m2', 'a1v1', 'a1v2', 'a2m1', 'a2m2', 'a2v1', 'a2v2',)
        exclude = ('id_enrolled', 'level', 'weeks')
        labels = {
            'n1m1': _('9:00 am - 10:30 am'),
            'n1m2': _('10:35 am - 12:05 pm'),
            'n2m1': _('9:00 am - 10:30 am'),
            'n2m2': _('10:35 am - 12:05 pm'),
            'b1m1': _('9:00 am - 10:30 am'),
            'b1m2': _('10:35 am - 12:05 pm'),
            'b2m1': _('9:00 am - 10:30 am'),
            'b2m2': _('10:35 am - 12:05 pm'),
            'i1m1': _('9:00 am - 10:30 am'),
            'i1m2': _('10:35 am - 12:05 pm'),
            'i1v1': _('3:30 pm - 5:00 pm'),
            'i1v2': _('5:05 pm - 6:35 pm'),
            'i2m1': _('9:00 am - 10:30 am'),
            'i2m2': _('10:35 am - 12:05 pm'),
            'i2v1': _('3:30 pm - 5:00 pm'),
            'i2v2': _('5:05 pm - 6:35 pm'),
            'a1m1': _('9:00 am - 10:30 am'),
            'a1m2': _('10:35 am - 12:05 pm'),
            'a1v1': _('3:30 pm - 5:00 pm'),
            'a1v2': _('5:05 pm - 6:35 pm'),
            'a2m1': _('9:00 am - 10:30 am'),
            'a2m2': _('10:35 am - 12:05 pm'),
            'a2v1': _('3:30 pm - 5:00 pm'),
            'a2v2': _('5:05 pm - 6:35 pm'),
        }

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
        fields = ('s1', 's2', 's3')
        exclude = ('id_enrolled', 'classes')
        labels = {
            's1': _('Taller 1'),
            's2': _('Taller 2'),
            's3': _('Taller 3'),
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