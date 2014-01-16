from django.shortcuts import render
from django.http import HttpResponse



#ch3
def home_page(request):
    return render(request, 'home.html')
