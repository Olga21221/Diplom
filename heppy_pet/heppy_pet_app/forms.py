from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=10)
    email = forms.EmailField()
    number = forms.ImageField(max_length=11)