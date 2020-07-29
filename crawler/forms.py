from django import forms

class handleForm(forms.Form):
    handle=forms.CharField(label='Enter the Codeforces Handle', max_length=150)
