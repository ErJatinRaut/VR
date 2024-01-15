from django.shortcuts import render

# Create your views here.

def seller_base(request):
    return render(request, "seller_base.html")

