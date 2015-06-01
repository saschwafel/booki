from .models import Book_Entry
from django import forms
from django.forms import ModelForm
from datetimewidget.widgets import DateTimeWidget
class EntryForm(ModelForm):
    class Meta:
        model = Book_Entry
        fields = ['title', 'author', 'date_added', 'date_started', 'date_finished']
        # fields = ['title', 'author']
        # fields =  ('__all__') 
        widgets = {
            #Use localization and bootstrap 3
            'datetime': DateTimeWidget(attrs={'id':"date_added"}, usel10n = True, bootstrap_version=3)
        }
