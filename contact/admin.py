from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
