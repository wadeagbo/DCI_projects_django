# import the forms module

from django import forms

# inherit from forms.Form

# organization
CAR_CHOICES = (
    ('bmw', "BMW"),
    ('tesla', "Tesla"),
    ('fiat', "Fiat"),
    ('audi', "Audi"),
)

class CarSearch(forms.Form):
    start_date = forms.DateField(label='When do you want to take car?', widget=forms.SelectDateWidget)
    end_date = forms.DateField(label='when to bring back car?', widget=forms.SelectDateWidget)
    cars = forms.CharField(initial="fiat", label="Choose your car", widget=forms.Select(choices=CAR_CHOICES), help_text="All our cars are premium, if you scratch you pay!")


class SearchForm(forms.Form):
    # TODO: add date support e.g. when money should arrive to the person you are sending it to.
    search_term = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget)

class HotelSearch(forms.Form):    
    start_date = forms.DateField(label='Checkin', widget=forms.SelectDateWidget)
    end_date = forms.DateField(label='Checkout', widget=forms.SelectDateWidget)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField() # some validations in frontend
    reason = forms.CharField(widget=forms.Textarea)