from django.db import models
from django.urls import reverse
# Create your models here.


class Menu(models.Model):
    category = (
        ("Issiq", "Issiq"),
        ("Sovuq", "Sovuq"),
    )
    img = models.ImageField(upload_to='images/')
    narxi = models.PositiveIntegerField()
    nomi = models.CharField(max_length=50)
    about = models.CharField(max_length=500)
    coffee_turi = models.CharField(choices=category, max_length=20)

    def __str__(self):
        return self.nomi

class Book_Your_Table(models.Model):
    select = (
        ("person1", "person1"),
        ("person2", "person2"),
        ("person3", "person3"),
        ("person4", "person4"),
    )
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    person = models.CharField(choices=select, max_length=30)

    def __str__(self):
        return self.person
    
    def get_absolute_url(self):
        return reverse('home')




class Contact(models.Model):
    ism = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.subject
    
    def get_absolute_url(self):
        return reverse('contact')











