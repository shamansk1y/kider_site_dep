"""
This module defines Django forms used for the main_page app.

MakeAppointmentForm is a ModelForm that allows users to make an appointment by providing their name,
email, child's name, child's age, and a message.

SubscriptionForm is a ModelForm that allows users to subscribe to a service by providing their email.

ContactUsForm is a ModelForm that allows users to contact the website administrators by providing their name,
email, subject, and message.

All forms define the fields to be displayed in the form and their corresponding HTML input attributes.
These forms are used to validate and process user input on the front-end and back-end of the website.

Attributes:
    - MakeAppointmentForm (class): A Django ModelForm for making appointments.
    - SubscriptionForm (class): A Django ModelForm for subscribing to a service.
    - ContactUsForm (class): A Django ModelForm for contacting the website administrators.

"""


from django import forms
from main_page.models import Appointment, Subscription, ContactUs


class MakeAppointmentForm(forms.ModelForm):
    name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control border-0",
                'id': "gname",
                'placeholder': "Gurdian Name",
                }))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'type': "email",
                'class': "form-control border-0",
                'id': "gmail",
                'placeholder': "Gurdian Email"
            }))

    child_name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control border-0",
                'id': "cname",
                'placeholder': "Child Name"}))

    child_age = forms.CharField(
        max_length=2,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control border-0",
                'id': "cage",
                'placeholder': "Child Age"}))

    message = forms.CharField(
        max_length=250,
        widget=forms.Textarea(
            attrs={
                'class': "form-control border-0",
                'placeholder': "Leave a message here",
                'id': "message",
                'style': "height: 100px",
                "message": 'Message'
            }))

    class Meta:
        model = Appointment
        fields = ['name', 'email', 'child_name', 'child_age', 'message']


class SubscriptionForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': "form-control bg-transparent w-100 py-3 ps-4 pe-5",
                'type': "text",
                'placeholder': "Your email"
            }))
    class Meta:
        model = Subscription
        fields = ['email']


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control border-0",
                'id': "name",
                'placeholder': "Your Name"
            }))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'type': "email",
                'class': "form-control border-0",
                'id': "email",
                'placeholder': "Your Email"
            }))

    subject = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control border-0",
                'id': "subject",
                'placeholder': "Subject"
            }))


    message = forms.CharField(
        max_length=300,
        widget=forms.Textarea(
            attrs={
                'class': "form-control border-0",
                'placeholder': "Leave a message here",
                'id': "message",
                'style': "height: 100px"
            }))

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']