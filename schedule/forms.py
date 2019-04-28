from django import forms
from .models import ClassEnrolled, User


class ClassEnrolledForm(forms.ModelForm):
    class Meta:
        model = ClassEnrolled
        fields = ('id_program', 'id_level', 'id_class')
        exclude = ('id_enrolled}',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
