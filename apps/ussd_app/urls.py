from django.urls import path
from . import views

urlpatterns = [
    path('', views.ussd_view, name='ussd_view'),
]
