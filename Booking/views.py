from django.shortcuts import render, redirect, get_object_or_404
from .models import Destination, Booking
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.http import Http404, JsonResponse
import json
import uuid


def index(request):
	destinations = Destination.objects.all().order_by("?")[:3]
	return render(request, "Booking/home.html", {"destinations": destinations})
	
	
def booking(request):
	destinations = Destination.objects.all().order_by("name")
	
	context = {
		"destinations": destinations
	}
	return render(request, "Booking/booking.html", context)
	
	
def getBookingData(request):
	response = json.loads(request.body)
	booking_id = uuid.uuid4()
	
	print(response)
	
	first_name = response["bookingData"]["first_name"]
	last_name = response["bookingData"]["last_name"]
	phone = response["bookingData"]["phone"]
	destination = response["bookingData"]["destination"]
	departure = response["bookingData"]["departure"]
	price = response["price"]
	
	print(Destination.objects.get(name= destination))
	
	if str(Destination.objects.get(name= destination).price) == price:
		Booking.objects.create(
			first_name= first_name,
			last_name= last_name,
			phone_no = phone,
			destination= Destination.objects.get(name= destination),
			date_of_departure = departure,
			active = True,
			booking_id= booking_id
		)
	
	return JsonResponse("Payment Successful", safe= False)
		

def complain(request):
	if request.method == "POST":
		subject = request.POST.get("subject")
		sender = request.POST.get("email")
		message = request.POST.get("complain")
		
		email = EmailMessage(
			subject,
			f"{sender}\n\n{message}",
			sender,
			["codewitgabi222@gmail.com"]
		)
		
		email.fail_silently = False
		email.send();
		return redirect("index")
		
	return render(request, "Booking/complain.html")