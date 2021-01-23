from django import forms

class RegisterForm(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    cpassword=forms.CharField(widget=forms.PasswordInput)
