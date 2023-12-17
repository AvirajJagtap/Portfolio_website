# admin.py
from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'subject', 'message')  # Display these fields in the admin list view
    search_fields = ('fname', 'lname', 'email', 'subject')  # Add fields for search functionality

# Register the Contact model with the custom admin class
admin.site.register(Contact, ContactAdmin)
