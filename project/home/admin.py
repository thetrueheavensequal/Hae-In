from django.contrib import admin
from . models import Departments, Doctors, Appointment, ContactMessage
# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(Appointment)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')  # Show all fields in admin panel
    search_fields = ('name', 'email')  # Enables search bar for these fields
admin.site.register(ContactMessage)