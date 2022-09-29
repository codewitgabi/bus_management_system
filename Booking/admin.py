from django.contrib import admin
from .models import Destination, Booking


class DestinationAdmin(admin.ModelAdmin):
	list_display = ["name", "price"]
	search_fields = ["name"]
	
	
class BookingAdmin(admin.ModelAdmin):
	list_display = ["first_name", "last_name", "phone_no", "date_of_departure", "active", "destination"]
	list_filter = ["date_of_departure", "active", "destination"]
	search_fields = ["destination"]
	
	
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Booking, BookingAdmin)