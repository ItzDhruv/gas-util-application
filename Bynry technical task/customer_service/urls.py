from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("submit/", views.submit_request, name='submit_request'),
    path('track/', views.track_request, name='track_request'),
]