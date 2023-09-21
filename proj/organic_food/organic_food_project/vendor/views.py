# vendor/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm, ProductForm

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process registration and redirect
            # You can use Django's built-in User model or a custom User model
            # Authenticate and log in the user if needed
            return redirect('vendor:login')
    else:
        form = RegistrationForm()
    return render(request, 'vendor/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Authenticate and log in the user
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('vendor:dashboard')  # Redirect to the dashboard
    else:
        form = LoginForm()
    return render(request, 'vendor/login.html', {'form': form})

def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Process product addition and redirect
            return redirect('vendor:dashboard')
    else:
        form = ProductForm()
    return render(request, 'vendor/add_product.html', {'form': form})
