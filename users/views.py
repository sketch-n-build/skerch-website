from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Welcome {request.user}, registrtion was successful')            
            return redirect('login')
        else:
            message = 'sorry something went wrong!'
            context = {
            'title':'Register',
            'form':form,
            'message':message
            }
            return render(request,'users/login.html',context)
    else:
        form = UserRegistrationForm()
        context = {
            'title':'Create Post',
            'form':form
        }
        return render(request,'users/register.html',context)
@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your profile has been updated!')
            return redirect('profile')
        else:
            messages.error(request,'something went wrong! form not valid')
            context = {
                'u_form':u_form,
                'p_form':p_form,
            }
            return render(request,'users/profile.html',context)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'title':'Profile',
            'u_form':u_form,
            'p_form':p_form,
        }
        return render(request,'users/profile.html',context)