from django import forms

class CheckList(forms.Form):
    check = forms.BooleanField(label_suffix='',required=False)
    name = forms.CharField(label='Hello')

    
