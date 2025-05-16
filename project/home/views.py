from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate,login as authlogin, logout as authlogout
from . models import Departments, Doctors, Appointment, ContactMessage
from . forms import AppmntForm, ContactForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect
from .models import Appointment

# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def apply(request):
    if not request.user.is_authenticated:
        return render(request, 'users/not_logged_in.html')
    
    if request.method == "POST":
        form = AppmntForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('status')  # ✅ inside the if block
    else:
        form = AppmntForm()

    return render(request, 'apply.html', {'form': form})

def status(request):
    user_appointments = Appointment.objects.filter(user=request.user).order_by('-appmnt_on')
    latest = user_appointments.first()
    return render(request, 'status.html', {'appointment': latest})


def doctors(request):
    dict_docs = {
        'doctors' : Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)
def department(request):
    dict_dept = {
        'dept' : Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Prevent resubmission on refresh
    else:
        form = ContactForm()

    contact_info = ContactMessage.objects.first()  # Static info for the clinic
    return render(request, 'contact.html', {
        'form': form,
        'contact_info': contact_info
    })
def signup(request):
    error_message = None
    created_user = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            error_message = "Username already taken. Please choose another."
        else:
            try:
                created_user = User.objects.create_user(username=username, password=password)
                return redirect('login')  # redirect to login after successful sign up
            except Exception as e:
                error_message = "An error occurred during signup. Please try again."

    return render(request, 'users/signup.html', {
        'error_message': error_message,
        'User': created_user
    })


def login(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            authlogin(request, user)
            return redirect('home')
        else:
            error_message = "Invalid credentials"

    return render(request, 'users/login.html', {'error_message': error_message})

def logout(request):
    authlogout(request)
    return render(request, 'users/login.html', {'error_message': "Logged out successfully."})

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # or whatever your profile URL name is
    else:
        form = ProfileForm(instance=user)

    appointments = Appointment.objects.filter(user=user).order_by('-appmnt_date')
    return render(request, 'users/profile.html', {
        'form': form,
        'appointments': appointments
    })