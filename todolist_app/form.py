from django import forms
from .models import TaskList
from django.db import models


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done']

