
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("customer_service.urls")),
    path("submit/",include("customer_service.urls")),
    path("track/",include("customer_service.urls"))
]
