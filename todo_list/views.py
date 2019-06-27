from django.shortcuts import render
from .models import List
from .forms import ListForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()

    # This has to happen regardless of request method, in order to fetch and display the list
    all_items = List.objects.all
    return render(request, 'home.html', {'all_items': all_items})

def about(request):
    context = {'fname': 'Jerry', 'lname': 'Howard'}
    return render(request, 'about.html', context)
