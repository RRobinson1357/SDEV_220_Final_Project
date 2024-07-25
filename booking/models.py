import datetime
from django.db import models
from django.conf import settings

#defines room class
class Room(models.Model):
    #list of options for the room_desc attribute
    #"desc" is a temporary value for a description of each room type
    room_style = {
        ("Basic", "desc"),
        ("Standard", "desc"),
        ("Studio", "desc"),
    }

    #attributes of the room class
    room_number = models.CharField(max_length = 3, null = False, unique = True, primary_key = True)
    window_number = models.CharField(max_length = 2, null = False)
    bed_number = models.CharField(max_length = 1, null = False)
    sq_ft = models.CharField(max_length = 4, null = False)
    occupants = models.CharField(max_length = 2, null = False)
    room_desc = models.CharField(max_length = 10, choices = room_style)
    rented = models.BooleanField(null = False)
    cost_per_night = models.DecimalField(max_digits = 5, decimal_places = 2)
  
    #i plan on adding the book function here, it would create an     instance of the 
    #rental class using the room number and user account
    '''def book(self, room_number, customer):
        self.hotel = Room.room_number.get()
        self.customer = settings.AUTH_USER_MODEL.get()'''

#defines rental class
#not sure how we will set up the booking dates so i might have to change this later
class Rental(models.Model):
    room_number = models.ForeignKey(Room, on_delete = models.CASCADE)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    start_date = models.DateTimeField(auto_now = False)
    end_date = models.DateTimeField(auto_now = False)
    total = models.DecimalField(max_digits = 9, decimal_places = 2)

class Dates(models.Model):
    room_number = models.ForeignKey(Room, on_delete = models.CASCADE)
    date_booked = models.DateTimeField(auto_now = False)
    
    def __str__(self):
        date = self.date_booked
        date = date.strftime("datetime.datetime(%Y, %#m, %#d, 0, 0 tzinfo=zoneinfo.ZoneInfo(keys='UTC))")
        return date