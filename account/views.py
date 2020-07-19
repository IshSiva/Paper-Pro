
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView,TemplateView
from .forms import AuthorRegistrationForm,UserLoginForm,ReviewerRegistrationForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,get_user_model
from django.contrib.auth import authenticate, login, logout
from .models import Author
from django.contrib.auth.decorators import login_required
from django.db import transaction



# Create your views here.

class Signup(TemplateView):
    template_name='account/choice.html'
    



def homepage(request):
    return render(request, 'account/index.html')


def registerAuthor(request):
    if request.method=='POST':
        form = AuthorRegistrationForm(request.POST, request.FILES) #instantiate the form

        if form.is_valid():
            auth_form = form.save() #save all the details
            auth_form.save() #save a pgr instance to the db
            return redirect('/account/login/')


        else:
            #if any of the details in the form is invalid we render the form again
            print(form.errors)
            return render(request,'account/signup.html', {'form':form}) 




        
    #if the url is called with a GET method we simply return the form    
    else:
        form = AuthorRegistrationForm()
        return render(request,'account/signup.html', {'form':form})

def registerReviewer(request):
    if request.method=='POST':
        form = ReviewerRegistrationForm(request.POST, request.FILES) #instantiate the form

        if form.is_valid():
            rev_form = form.save() #save all the details
            rev_form.save() #save a pgr instance to the db
            return redirect('/account/login/')


        else:
            #if any of the details in the form is invalid we render the form again
            print(form.errors)
            return render(request,'account/signuprev.html', {'form':form}) 




        
    #if the url is called with a GET method we simply return the form    
    else:
        form = AuthorRegistrationForm()
        return render(request,'account/signuprev.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('/')


def user_login(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username=username, password=password)

        login(request, user)
        
        if user.isauthor:
            url = "/db/authordboard/"
            print(url)
            return redirect(url)

        elif user.isreviewer:
            url = "/db/reviewdboard/"
            return redirect(url)            


        elif user.iseditor:
            url = "/db/editordboard/"
            return redirect(url)

        return redirect('/account/login/')

    context = {
        'form': form,
    }
    print(form.errors)
    return render(request, "account/login.html", context)
