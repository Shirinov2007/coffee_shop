from django.urls import path 
from .views import * 

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('about/', About.as_view(), name = "about"),
    path('contact/', Contact.as_view(), name="contact"),
    path('menu/', Menu_View.as_view(), name="menu"),
    path('reservation/', Reservation.as_view(), name="reservation"),
    path('service/', Service.as_view(), name="service"),
    path("testimonial/", Testimonial.as_view(), name="testimonial"),

]