from django.shortcuts import render

# Create your views here.
def bootstrap_cus(request):
    return render(request, "customer_base.html")