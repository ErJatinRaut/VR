from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('customer_base/',bootstrap_cus,name="bootstrap_cus"),
]