from django import forms


class HoroscopeForm(forms.Form):
    # sign
    sign = forms.CharField(label='Your sign')