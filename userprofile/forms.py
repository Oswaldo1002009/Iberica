from django import forms
from schedule.models import Enrolled
from django.utils.translation import ugettext_lazy as _

class DateInput(forms.DateInput):
    input_type = 'date'

class CompleteProfile(forms.ModelForm):
    class Meta:
        model = Enrolled
        exclude = ['user']
        labels = {
            'name': _('Nombre(s)'),
            'lastname': _('Apellidos'),
            'birth_date': _('Fecha de nacimiento'),
            'gender': _('Género'),
            'phone': _('Teléfono'),
            'address': _('Dirección'),
            'city': _('Ciudad'),
            'country': _('País'),
            'zip_code': _('Código Postal'),
            'academy': _('Academia'),
            'disease': _('Enfermedades'),
            'blood_type': _('Tipo de sangre'),
        }
        widgets = {
            'birth_date': DateInput(),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
