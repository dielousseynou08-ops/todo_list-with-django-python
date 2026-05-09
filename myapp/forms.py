
from django import forms
from .models import Mytodo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Mytodo
        fields = ['title', 'content']
        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-input',
                'placeholder': 'Ajouter une nouvelle tâche...',
                'autofocus': True,

            }),
            'content': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Description (optionnelle)',
                'rows': 3,
            })
        }