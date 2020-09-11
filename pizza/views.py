from django.shortcuts import render

# Create your views here.
# 5. Add request function for home page
def home (request):
    return render(request,'pizza/home.html')

# 6. Add request function for order page
def order (request):
    return render(request,'pizza/order.html')