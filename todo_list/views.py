from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item has been added to the list')

    # This has to happen regardless of request method, in order to fetch and display the list
    all_items = List.objects.all
    return render(request, 'home.html', {'all_items': all_items})

def about(request):
    context = {'fname': 'Jerry', 'lname': 'Howard'}
    return render(request, 'about.html', context)

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete() 
    # ^^ Remember, you're not running a delete operation on a table, but an object representing
    # a row in the table.
    messages.success(request, 'Item has been deleted')
    return redirect('home')

