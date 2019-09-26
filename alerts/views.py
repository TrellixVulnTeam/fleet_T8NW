from django.shortcuts import render
from vehicles.models import vehicle
from .models import Alert

def alert_function(request):
    for e in vehicle.objects.filter(speed__gte=65):
        a = Alert()
        a.vehicle_id = e.plateNumber
        a.latitude = e.latitude
        a.longtude = e.longitude
        a.alert_name = "speeding over 65"
        a.alert_type = "Speed"
        a. priority = "LOW"
        a.action = "None"
        a.save()
    return render(request,'alerts/alerts.html')