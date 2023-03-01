"""
This module contains two Django form classes: UserLogin and UserRegistration.

UserLogin is a form for authenticating user login credentials. It takes a username and password input from the user,
verifies that the username and password are valid, and raises a ValidationError if they are not.

UserRegistration is a form for creating new user accounts. It takes a username, password, and password confirmation
input from the user, verifies that the passwords match, and raises a ValidationError if they do not.

Inputs:
- UserLogin form: username (str), password (str)
- UserRegistration form: username (str), password (str), password2 (str)
"""


from django import forms
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()

class UserLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                raise forms.ValidationError('Error in Login or Password')
        else:
            raise forms.ValidationError('Error in Login or Password')
        return super().clean()


class UserRegistration(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username',)

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data['password2']
        raise forms.ValidationError('Error in password!')