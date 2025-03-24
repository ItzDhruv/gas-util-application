from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    # Add other fields as needed

class ServiceRequest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50)
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)  # Add this line for attachment
    # Add other fields as needed
