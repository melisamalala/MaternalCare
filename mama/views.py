from django.shortcuts import HttpResponse, render, redirect, get_object_or_404, reverse, get_list_or_404
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import mail_admins
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .forms import *
from .models import *
import datetime


# -- Authentication views

def login(request):
    if request.user.is_authenticated():
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'auth/login.html')


def logout(request):
    print('logout')
    auth.logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    form = MyRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)


# -- General Pages views


def home(request):
    return render(request, 'index.html')


def search_doctors(request):
    search_form = SearchDoctorsForm()
    doctors = []

    if 'search_term' in request.GET and request.GET['search_term']:
        search_term = request.GET.get('search_term')
        doctors = Doctor.search_doctors_by_term(search_term)

    context = {
        'search_form': search_form,
        'doctors': doctors
    }
    return render(request, 'doctors_search.html', context)


def individual_doctors_page(request, doctor_id, doctor_name):
    doctor = Doctor.get_one_doctor(doctor_id)
    context = {
        'doctor': doctor
    }
    return render(request, 'doctor_page.html', context)
