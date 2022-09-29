from django.db import models


class Booking(models.Model):
	first_name = models.CharField("First Name", max_length= 100)
	last_name = models.CharField("Last Name", max_length= 100)
	phone_no = models.CharField("Phone Number", max_length= 11)
	destination = models.ForeignKey("Destination", on_delete= models.SET_NULL, null= True)
	date_of_departure = models.DateField()
	active = models.BooleanField(default= False)
	booking_id = models.CharField(max_length= 37)
	
	
	def __str__(self):
		return self.first_name
		
		
		
class Destination(models.Model):
	name = models.CharField(max_length= 10)
	price = models.DecimalField(max_digits= 8, decimal_places= 2)
	
	
	def __str__(self):
		return self.name