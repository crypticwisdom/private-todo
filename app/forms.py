from django import forms
from django.db.models import fields
from django.db.models.base import Model
from app.models import TodoModel
from django.forms import ModelForm, widgets
from django import forms

class TodoForm(ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Title ...'

    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'style':'border-radius:5px;',
        'placeholder':'Description ...',
        'rows':'10',
        'cols':'25',

    }))
    class Meta:

        model = TodoModel
        exclude = ('user', 'completed')