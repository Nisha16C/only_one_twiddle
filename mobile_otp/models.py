from django.db import models
from django.contrib.auth.models import User

class PhoneNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)  # Adjust the max_length as needed
    is_primary = models.BooleanField(default=False)
    # Add any other fields you need, like 'country_code', 'verified', etc.

    def __str__(self):
        return self.phone_number
    
    
    
    
    