from django.shortcuts import render
def add_trip(request):
    return render(request, 'trip/add_trip.html')
