from django import forms


class FollowForm(forms.Form):
    username = forms.CharField(required=True)