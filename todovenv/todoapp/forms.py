from django import forms
from django.forms import ModelForm, DateInput
from .models import Todo

class UpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Todo
        fields = ['task', 'priority', 'date', 'desc']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }
