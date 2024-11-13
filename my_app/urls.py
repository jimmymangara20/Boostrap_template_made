
from django.urls import path
from . import views
app_name='myapp'
urlpatterns=[
    path('',views.index,name="index"),
    path('about/',views.about_us,name="about"),
    path('agents/',views.agents,name="agents"),
    path('contact/',views.contact_us,name="contact"),
    path('properties/',views.properties,name="properties"),
    path('services/',views.services,name="services"),
    path('communication',views.communication,name="communication"),
   
]