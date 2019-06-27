from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def about(request):
    context = {'fname': 'Jerry', 'lname': 'Howard'}
    return render(request, 'about.html', context)
