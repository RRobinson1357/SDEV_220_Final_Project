from datetime import timedelta

import django
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import Book_Date
from .models import Dates, Room


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})
def register(response):
    form = UserCreationForm()
    return render(response, 'registration/register.html', {'form':form})

def room_detail(request, room_number):
    room = get_object_or_404(Room, room_number = room_number)
    return render(request, 'room_view.html', {'room': room})

def BookRoom(request, room_number):
    room = room_number 
    context = {'room_number' : room}

    #instantiates form
    form = Book_Date(request.POST or None, request.FILES or None, initial = context)

    #Pulls dates the room is booked from the database
    dates_to_block = []
    block_room = Dates.objects.filter(room_number = room)
    block_room = block_room.values('date_booked')

    #compiles dates into a list of dictionary entries
    for date in block_room:
        dates_to_block.append(date)

    #formats list entries into string values so they can be compared later on
    blocked_dates = []
    for entry in dates_to_block:
        block_room = entry.values()
        block_room = str(block_room)
        block_room = block_room[13:-33]
        block_room = block_room + " tzinfo=zoneinfo.ZoneInfo(keys='UTC))"
        blocked_dates.append(block_room)
        print(block_room)

    print("blocked_dates ",blocked_dates)

    #validates form and supplies Rental variables not included in the form
    #forms do not get saved yet. they need to be saved after entering payment info
    if form.is_valid():
        booking = form.save(commit = False)
        booking.room_number = Room.objects.get(room_number = room)
        booking.customer = request.user
        room = Room.objects.get(room_number = room)

        #calculates price
        price = room.cost_per_night
        end = booking.end_date.date()
        start = booking.start_date.date()
        booking.total = ((end - start).days) * price

        #initializes input validation variables
        booked_flag = False
        date_flag = False

        if booking.start_date >= booking.end_date:
            messages.error(request,"The start date must be earlier than the end date.")
            date_flag = True

        #creates list of each date that will be booked
        delta = timedelta(days = 1)
        dates_requested = []

        while booking.start_date <= booking.end_date:
            dates_requested.append(booking.start_date)
            booking.start_date += delta

        #create list with strings representing te dates
        #so they can be compared with the blocked_dates list
        compare_date = []
        for date in dates_requested:
            date = date.strftime("datetime.datetime(%Y, %#m, %#d, 0, 0 tzinfo=zoneinfo.ZoneInfo(keys='UTC))")
            compare_date.append(date)

        print("compare date:",compare_date)

        #checks dates in compare_date list to those in database
        for date in compare_date:      
            print(date)
            if date in blocked_dates:
                #prevents user from double booking one date NEEDS ERROR MESSAGE
                booked_flag = True
                messages.error(request, "This room is not available to book during those dates.")
                break
        if booked_flag == False and date_flag == False:
            for date in dates_requested:
                #instantiates date to be sent to database
                #DOES NOT SAVE. might need to be added to list to save later?
                new_date = Dates(room_number = room, date_booked = date)



    #renders form
    context['form'] = form
    return render(request, 'rental_form.html', context)