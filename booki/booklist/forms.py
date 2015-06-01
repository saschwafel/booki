from .models import Book_Entry
from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from datetimewidget.widgets import DateTimeWidget


class EntryForm(ModelForm):
    class Meta:
        model = Book_Entry
        fields = ['title', 'author', 'date_added', 'date_started', 'date_finished']
        # fields = ['title', 'author']
        # fields =  ('__all__') 
        widgets = {
            'date_added': forms.DateInput(attrs={'type':'date'}),
            'date_started': forms.DateInput(attrs={'type':'date'}),
            'date_finished': forms.DateInput(attrs={'type':'date'})
        }
