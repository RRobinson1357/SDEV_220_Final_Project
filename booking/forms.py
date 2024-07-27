from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms

from .models import Rental

#defines Book_Date form
class Book_Date(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['start_date', 'end_date']
        template_name = 'rental_form.html'
        widgets = {
            'start_date': DatePickerInput(options={"format": "MM/DD/YYYY"}),
            'end_date': DatePickerInput(options={"format": "MM/DD/YYYY"}),
        }