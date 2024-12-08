from django import forms
from django.contrib.auth.models import User

class Registration(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput,label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,label="Password confirmation ")

    class Meta:
        model = User
        fields = ['username','email']

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords doesn't match")
        return password2