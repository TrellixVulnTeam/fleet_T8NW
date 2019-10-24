from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app_auth.views import funclu,get_temp,get_dataframe
import json

@csrf_exempt
def add_trip(request):
    print("success")
    temp = get_temp()
    y1 = json.loads(temp)
    df1 = get_dataframe(y1)
    i,j = funclu(df1)

    if request.is_ajax():
            message = "Yes, AJAX!"
    else:
            message = "Not Ajax"

    print(message)

    context = {
        "json" : j,
        "message":message,
    }
    return render(request, 'trip/add_trip.html',context)
