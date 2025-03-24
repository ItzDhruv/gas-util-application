from .models import ServiceRequest  # Update the import statement
from django import forms

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['type', 'description', 'attachment']  # Include 'attachment' field if needed
