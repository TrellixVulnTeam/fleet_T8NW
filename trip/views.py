from django.shortcuts import render
from app_auth.views import funclu,get_temp,get_dataframe
import json

def add_trip(request):
    temp = get_temp()
    y1 = json.loads(temp)
    df1 = get_dataframe(y1)
    i,j = funclu(df1)
    context = {
        "json" : j,
    }
    return render(request, 'trip/add_trip.html',context)
