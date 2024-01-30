from django.shortcuts import render
from myApp.models import Employee
from django.db.models import Q
from django.db.models import Avg, Max, Min, Sum, Count
from django.db.models.functions import Lower

# Create your views here.
def displayView(request):

    # employees = Employee.objects.filter(~Q(esal__range = (40000, 60000)))
    # print(type(employees))
    # qs1 = Employee.objects.filter(esal__lt = 60000)
    # qs2 = Employee.objects.filter(ename__endswith = 'R')
    # employees = qs1.union(qs2)
    # employees = Employee.objects.all()
    # employees = Employee.objects.get_emp_sal_range(40000, 60000)
    # employees = Employee.objects.get_emp_sorted_by('ename')
    dict = {'employees' : employees}

    return render(request, 'myApp/index.html', dict)

def agregate_view(request):

    eavg = Employee.objects.aggregate(Avg('esal'))
    emin = Employee.objects.aggregate(Min('esal'))
    emax = Employee.objects.aggregate(Max('esal'))
    esum = Employee.objects.aggregate(Sum('esal'))
    ecount = Employee.objects.aggregate(Count('esal'))

    agr_dict = {'avg':eavg, 'max':emax, 'min':emin, 'sum':esum, 'count':ecount}

    return render(request, 'myApp/aggregate.html', agr_dict)

