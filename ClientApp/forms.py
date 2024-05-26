from django import forms
from .models import Client, Project

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['client', 'name', 'description', 'users']
