from django import forms
from .models import StudentResult

class ResultForm(forms.ModelForm):
    class Meta:
        model = StudentResult
        fields = ['full_name', 'student_id', 'result']