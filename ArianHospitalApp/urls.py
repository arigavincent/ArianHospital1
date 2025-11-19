from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='Home'),
    path('About/',views.About,name='About'),
    path('Admin/',views.Admin,name='Admin'),
    path('Appointments/',views.Appointments,name='Appointments'),
    path('Contacts/',views.Contacts,name='Contacts'),
    path('Services/',views.Services,name='Services'),
    path('Doctors/',views.Doctors,name='Doctors'),
    path('Departments/',views.Departments,name='Departments'),
    path('Forgot',views.Forgot,name='Forgot'),

]