from django.shortcuts import render

# Create your views here.

def data_home(request):
    return render(request, 'booking/about.html')