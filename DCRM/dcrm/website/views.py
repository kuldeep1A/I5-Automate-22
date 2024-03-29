from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignupForm, AddRecordForm
from .models import Records


def home(request):
    records = Records.objects.all()
    # Check to see if loging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignupForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def customer_records(request, pk):
    if request.user.is_authenticated:
        # Look up records
        customer_record = Records.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You Must Been Logged In To View That Page..")
        return redirect('home')


def delete_records(request, pk):
    if request.user.is_authenticated:
        delete_it = Records.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect('home')


def add_records(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            form.save()
            messages.success(request, "Record Added...")
            return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In..")
        return redirect('home')


def update_records(request, pk):
    if request.user.is_authenticated:
        curr_record = Records.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=curr_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Records has been updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In..")
        return redirect('home')
