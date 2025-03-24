from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest

def home(request):
    context={}
    return render(request, "customer_service/Home.html", context)

@login_required
def submit_request(request):
    if request.method == 'POST':
        # Process form submission
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new service request
            # Example: service_request = form.save(commit=False)
            # Then set any additional fields and save the object
            # Example: service_request.customer = request.user.customer
            # service_request.save()
            # Redirect to a success page or show a confirmation message
            return redirect('track_request')
    else:
        # Render form for submitting requests
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_request.html', {'form': form})


@login_required
def track_request(request):
    # Retrieve service requests for the current user
    service_requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'customer_service/track_request.html', {'service_requests': service_requests})