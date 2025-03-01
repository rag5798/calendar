from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_description', 'task_date', 'task_time']
        widgets = {
            'task_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }
