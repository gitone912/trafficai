from django.urls import path
from . import views

app_name = 'traffic'

urlpatterns = [
    path('intersection/<int:intersection_id>/', views.intersection_traffic, name='intersection_traffic'),
    path('', views.home, name='home'),
    path('release_side/', views.release_side, name='release_side'),
    # Add other URL patterns as needed
]
