from django.shortcuts import render
from .models import Employee, Transaction
from django.contrib.auth import (login as auth_login,  authenticate)
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms	import TransactionForm

def mainpage(request):
	employees = Employee.objects.all().order_by('name')
	transactions = Transaction.objects.all().order_by('-date')
	form = TransactionForm()
	form.fields["receiver"].queryset = Employee.objects.exclude(name_id=request.user.id)

	return render(request, 'thanks/mainpage.html', {'employees': employees, 'transactions': transactions, 'form': form})

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

def give_points(request):
	form = TransactionForm(request.POST)

	if form.is_valid():
		transaction = form.save(commit=False)
		loggedUserId = request.user.id
		giv = Employee.objects.get(name_id=loggedUserId)

		transaction.giver = giv
		transaction.save()

		rec2 = Employee.objects.get(id=transaction.receiver_id)
		rec2.points_collected += transaction.points_given
		giv.points_to_give -= transaction.points_given
		rec2.save()
		giv.save()

		form = TransactionForm()
		return mainpage(request)

	args = {'employees': employees,  'transactions': transactions, 'form': form}
	return render(request, 'thanks/mainpage.html', args)
