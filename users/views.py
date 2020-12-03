from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import (
    NewUserCreationForm,
    UserUpdateForm,
    UserProfileUpdateForm,
)

from django.contrib import messages


from django.contrib.auth.decorators import login_required


from django.contrib.auth.views import LoginView
# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account created successfully')
            return redirect('login')
    else:
        form = NewUserCreationForm()
    context = {
        'title': 'Register',
        'form': form
    }
    return render(request, 'register.html', context)


@login_required(login_url="login")
def profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = UserProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)
