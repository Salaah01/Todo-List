from django import forms

class TasksForm(forms.Form):
    task_name = forms.CharField(max_length=100)