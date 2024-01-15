from django.urls import path, include,re_path
from .views import *

urlpatterns = [
    path("customer_register/",cust_registeration,name="cust_registeration"),
    path("customer_login/",cust_login,name="customer_login"),
    path("customer_after_login/",customer_after_login,name="customer_after_login"),
    path("seller_registeration/",seller_registeration,name="seller_registeration"),
    path("seller_login/",seller_login,name="seller_login"),
    path("seller_dashboard/",seller_dashboard,name="seller_dashboard"),
    path("admin_login/",admin_login,name="admin_login"),
    path("admin_dashboard/",admin_dashboard,name="admin_dashboard"),


]