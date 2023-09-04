from django.contrib import admin

# Register your models here.
from .models import PhoneNumber

class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'is_primary')


admin.site.register(PhoneNumber,PhoneNumberAdmin)