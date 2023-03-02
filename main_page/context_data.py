"""
Module containing functions related to obtaining page context.

Functions:
- get_common_context: gets the common page context used across multiple pages of the site.
- get_page_context: gets the page context with the current request taken into account.
"""


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
        'about': About.objects.get(id=1),
        'testimonial': Testimonial.objects.filter(is_visible=True),
        'classes': Classes.objects.all().order_by('?')[:6],
        'facilities': Facilities.objects.get(id=1),
        'call': Call.objects.get(id=1),
        'gallery': Gallery.objects.all().order_by('?')[:6],
        'contacts': Contacts.objects.get(id=1),
        'make_appointment': MakeAppointmentForm(),
        'subscription': SubscriptionForm(),
        'contact_us': ContactUsForm(),
        'schedule': Schedule.objects.get(id=1),
        'headlines': Headlines.objects.get(id=1),
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
    return data
