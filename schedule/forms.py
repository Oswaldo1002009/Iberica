from django import forms
from .models import ClassEnrolled, Groups, TallerGuitarra
from django.utils.translation import ugettext_lazy as _

class TallerGuitarraForm(forms.ModelForm):
    class Meta:
        model = TallerGuitarra
        fields = ('id_class',)
        exclude = ('id_enrolled',)
        labels = {
            'id_class': _('Taller'),
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