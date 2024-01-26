from django.shortcuts import render
from myApp.models import Employee
from django.db.models import Q

# Create your views here.
def displayView(request):

    employees = Employee.objects.filter(~Q(esal__range = (40000, 60000)))
    # print(type(employees))
    dict = {'employees' : employees}

    return render(request, 'myApp/index.html', dict)

