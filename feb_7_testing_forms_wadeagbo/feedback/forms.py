from django import forms
from .models import Feedback

class AddFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback         # as instance
        fields = ['email', 'name', 'message']