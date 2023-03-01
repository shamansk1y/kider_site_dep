from django.urls import path
from main_page.views import index, update_manager, manager_list

app_name = 'main_page'



urlpatterns = [
    path('', index, name='index'),
    path('manager/update_manager/<int:pk>', update_manager, name='update_manager'),
    path('manager/manager_list/', manager_list, name='manager_list'),
    ]