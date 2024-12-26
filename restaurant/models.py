from django.db import models

class Booking(models.Model):
    ID = models.AutoField(primary_key=True)  
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

class Menu(models.Model):
    ID = models.AutoField(primary_key=True)  
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(decimal_places=2, max_digits=6) 
    Inventory = models.IntegerField() 

