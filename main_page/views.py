"""
This module defines several views and helper functions for the website. The views include the following:
- `index(request)`: renders the homepage of the website.
- `about(request)`: renders the 'about us' page of the website.
- `contacts(request)`: renders the 'contact us' page of the website.
- `classes(request)`: renders the 'classes' page of the website.
- `join_us(request)`: renders the 'join us' page of the website.
- `schedule(request)`: renders the 'schedule' page of the website.
- `update_manager(request, pk)`: a view that updates the processed status of subscription,
contact us and appointment requests.
- `manager_list(request)`: a view that renders the list of unprocessed subscription,
contact us and appointment requests for the website manager.

The following helper functions are also defined:
- `is_manager(user)`: a helper function that returns `True` if the user belongs to the 'manager' group.
- `handle_post_request(request)`: a helper function that processes form data received from POST requests
and saves the data if it is valid.
"""

from django.shortcuts import render, redirect
from .forms import MakeAppointmentForm, SubscriptionForm, ContactUsForm
from .models import Subscription, ContactUs, Appointment
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import MakeAppointmentForm, SubscriptionForm, ContactUsForm
from .models import Slider, Team, About, Testimonial, Classes, Facilities, Call, Gallery, Contacts, Schedule, Headlines


def get_common_context():
    """
    Gets the common page context used across multiple pages of the site.
    :return:
    """
    return {
        'slider': Slider.objects.filter(is_visible=True),
        'team': Team.objects.all()[:3],
        'about': About.objects.get(),
        'testimonial': Testimonial.objects.filter(is_visible=True),
        'classes': Classes.objects.all().order_by('?')[:6],
        'facilities': Facilities.objects.get(),
        'call': Call.objects.get(),
        'gallery': Gallery.objects.all().order_by('?')[:6],
        'contacts': Contacts.objects.get(),
        'make_appointment': MakeAppointmentForm(),
        'subscription': SubscriptionForm(),
        'contact_us': ContactUsForm(),
        'schedule': Schedule.objects.get(),
        'headlines': Headlines.objects.all(),
    }


def get_page_context(request):
    """
    Gets the page context with the current request taken into account.

    Args:
    - request: HttpRequest object.

    Returns:
    - tuple of two elements:
        - dictionary containing data specific to the current request:
            'user_manager': True if the user is in the 'manager' group, False otherwise.
            'user_auth': True if the user is authenticated, False otherwise.
        - dictionary containing the common page context obtained from the get_common_context function.
    """
    data = {
        'user_manager': request.user.groups.filter(name='manager').exists(),
        'user_auth': request.user.is_authenticated,
    }
    context = get_common_context()
    data.update(context)
    return data, context

def is_manager(user):
    return user.groups.filter(name='manager').exists()

def handle_post_request(request):

    make_appointment = MakeAppointmentForm(request.POST)
    contact_us = ContactUsForm(request.POST)
    subscription = SubscriptionForm(request.POST)

    if make_appointment.is_valid():
        make_appointment.save()
        return redirect('/')
    if contact_us.is_valid():
        contact_us.save()
        return redirect('/')
    if subscription.is_valid():
        subscription.save()
        return redirect('/')

def index(request):
    if request.method == 'POST':
        handle_post_request(request)

    data, context = get_page_context(request)
    return render(request, 'index.html', context=data)

def about(request):
    if request.method == 'POST':
        handle_post_request(request)

    data, context = get_page_context(request)
    return render(request, 'about.html', context=data)

def contacts(request):
    if request.method == 'POST':
        handle_post_request(request)

    data, context = get_page_context(request)
    return render(request, 'contact.html', context=data)

def classes(request):
    if request.method == 'POST':
        handle_post_request(request)

    data, context = get_page_context(request)
    return render(request, 'classes.html', context=data)

def join_us(request):
    if request.method == 'POST':
        handle_post_request(request)

    data, context = get_page_context(request)
    return render(request, 'join_us.html', context=data)


def schedule(request):
    if request.method == 'POST':
        handle_post_request(request)

    data, context = get_page_context(request)
    return render(request, 'schedule.html', context=data)



@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_manager(request, pk):
    Subscription.objects.filter(pk=pk).update(is_processed=True)
    ContactUs.objects.filter(pk=pk).update(is_processed=True)
    Appointment.objects.filter(pk=pk).update(is_processed=True)
    return redirect('main_page:manager_list')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def manager_list(request):
    subscription_viev_manager = Subscription.objects.filter(is_processed=False)
    contact_us_viev_manager = ContactUs.objects.filter(is_processed=False)
    make_appointment_viev_manager = Appointment.objects.filter(is_processed=False)
    data = {
        'subscription_viev_manager': subscription_viev_manager,
        'make_appointment_viev_manager': make_appointment_viev_manager,
        'contact_us_viev_manager': contact_us_viev_manager,
    }
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'manager.html', context=data)