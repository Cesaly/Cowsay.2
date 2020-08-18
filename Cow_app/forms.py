from django import forms


class CowTextForm(forms.Form):
    text = forms.CharField(max_length=60)
