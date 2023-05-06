from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .models import *
# Create your views here.

class Home(TemplateView):
    template_name = "index.html"

class About(TemplateView):
    template_name = "about.html"

class Contact(CreateView):
    model = Contact
    template_name = "contact.html"
    fields = "__all__"
    

class Menu_View(ListView):
    model = Menu
    template_name = "menu.html"

class Reservation(CreateView):
    model = Book_Your_Table
    template_name = "reservation.html"
    fields = "__all__"

class Service(TemplateView):
    template_name = "service.html"

class Testimonial(TemplateView):
    template_name = "testimonial.html"
