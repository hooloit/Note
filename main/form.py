from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django import forms
#
#
# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ведите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ведите описание '
            })
        }