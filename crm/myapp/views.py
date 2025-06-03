from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm , AddRecordForm  # Assuming you have a SignUpForm in forms.py
from .models import Record  # Import your model if needed
# Create your views here.

def homepage(request):
    records = Record.objects.all()  # Fetch all records from the database
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('homepage')
        else:
            messages.success(request, 'There was an error logging in. Please try again.')
            return redirect('homepage')
    # If not logging in, render the homepage
    else:
        return render(request, 'index.html' , {'records': records} )  # Pass records to the template



def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('homepage')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate the new user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect('homepage')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
        
    return render(request, 'register.html')  # Render registration form

def customer_record(request, pk):
    if request.user.is_authenticated:
        # If the user is authenticated, proceed to fetch the record
        customer_record = Record.objects.get(id=pk)  # Fetch the record by id as primary key
        return render(request, 'record.html', {'customer_record':customer_record })  # Pass the record to the template
    else:
        # If the user is not authenticated, redirect to the homepage
        messages.success(request, 'You must be logged in to view customer records.')
        return redirect('homepage')
    

def delete_record(request, pk):
    if request.user.is_authenticated:
        # If the user is authenticated, proceed to delete the record
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfully.')
        return redirect('homepage')
    else:
        # If the user is not authenticated, redirect to the homepage
        messages.success(request, 'You must be logged in to delete records.')
        return redirect('homepage')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record added successfully.')
                return redirect('homepage')
        return render(request, 'add_record.html' , {'form': form})
    else:
        messages.success(request, 'You must be logged in to add records.')
        return redirect('homepage')
    

def update_record(request , pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record updated successfully.')
                return redirect('homepage')
        return render(request, 'update_record.html', {'form': form})