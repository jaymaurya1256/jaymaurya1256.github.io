from django.shortcuts import render
from flights.models import Flight
# Create your views here.

def index(request):
    D={"flights":Flight.objects.all()}
    return render(request,"flights/index.html",D)
def flight(request,flight_id):
    flight=Flight.objects.get(id=flight_id)
    return render(request,"flights/flight.html",{
        "flight":flight
    })

