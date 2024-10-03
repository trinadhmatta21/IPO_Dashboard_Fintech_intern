from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import IPO
from .forms import IPOForm
from django.http import HttpResponseForbidden

def is_superuser(user):
    if not user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    return True

# View for signin
def signin_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Get the user by email
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User with this email does not exist.')
            return redirect('signin')

        # Authenticate using the username (from the user object) and the password
        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)  # Log the user in
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('dashboard')  # Redirect to the dashboard
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('signin')

    return render(request, 'signin.html')

# View for signup
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the user already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('signup')

        # If user does not exist, create a new one
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Signup successful. Please sign in.')
        return redirect('signin')

    return render(request, 'signup.html')
@login_required
def dashboard_view(request):
    username = request.user.username  # Get the logged-in user's username
    return render(request, 'dashboard.html', {'username': username})
@login_required  # This ensures that the user must be logged in to access this view
def manage_ipo(request):
    # Retrieve IPOs from the database (this part is assumed)
    ipos = IPO.objects.all()  # Replace this with your actual model/query
    return render(request, 'accounts/manage_ipo.html', {
        'ipos': ipos,
        'user': request.user  # Pass the current user
    })

@login_required  # This ensures that the user must be logged in to access this view
def register_ipo(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    if request.method == 'POST':
        # Handle the registration of the IPO
        # Save IPO data logic here
        pass

    return render(request, 'accounts/register_ipo.html', {
        'user': request.user  # Pass the current user
    })
def userside_ipo(request):
    ipos = IPO.objects.all()
    return render(request, 'accounts/userside_ipo.html', {'ipos': ipos})