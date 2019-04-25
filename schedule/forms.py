from django import forms
from .models import ClassEnrolled, Level

class ClassEnrolledForm(forms.ModelForm):
    class Meta:
        model = ClassEnrolled
        fields = ('id_program', 'id_level', 'id_class', 'id_enrolled')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_level'].queryset = Level.objects.none()

        if 'id_ program' in self.data:
            try:
                program_id = int(self.data.get('id_program'))
                self.fields['id_level'].queryset = Level.objects.filter(program_id=program_id).order_by('level')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['id_level'].queryset = self.instance.program.level_set.order_by('level')
