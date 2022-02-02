from django.urls import path
from . import views


app_name = 'vendor'


urlpatterns = [
    path('become_vendor/', views.become_vendor, name="become_vendor")
    ]
