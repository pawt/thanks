from django.shortcuts import render
from .models import Employee

def mainpage(request):
	employees = Employee.objects.all().order_by('name')
	return render(request, 'thanks/mainpage.html', {'employees': employees})
