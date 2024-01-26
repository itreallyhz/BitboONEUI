from django.shortcuts import render, redirect
from django.http import JsonResponse



# Create your views here.
def index(request):
    return render(request, 'index.html', {'current_page': 'index'})
def navbar(request):
    return render(request, 'navbar.html')
def footer(request):
    return render(request, 'footer.html')
def about(request):
    return render(request, 'about.html', {'current_page': 'about'})
def service(request):
    return render(request, 'service.html')
def standard_services(request):
    return render(request, 'standard_services.html')
def enterprise_services(request):
    return render(request, 'enterprise_services.html')

def contact(request):
    return render(request, 'contact.html')