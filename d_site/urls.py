"""d_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main_page.views import about, contacts, classes, join_us, schedule
from account.views import registration_view, login_view, logout_view


urlpatterns = [
    path('', include('main_page.urls')),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('classes/', classes, name='classes'),
    path('join_us/', join_us, name='join_us'),
    path('logout/', logout_view, name='logout_view'),
    path('login/', login_view, name='login_view'),
    path('registration/', registration_view, name='registration_view'),
    path('schedule/', schedule, name='schedule'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)