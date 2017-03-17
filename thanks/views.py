from django.shortcuts import render
from .models import Employee
from django.contrib.auth import (login as auth_login,  authenticate)
from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def mainpage(request):
	employees = Employee.objects.all().order_by('name')
	return render(request, 'thanks/mainpage.html', {'employees': employees})

def login(request):
    _message = 'Please sign in'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('mainpage'))
            else:
                _message = 'Your account is not activated!'
        else:
            _message = 'Invalid login, please try again.'
    context = {'message': _message}
    return render(request, 'thanks/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')