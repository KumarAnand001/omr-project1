from django.db import models
from django.db.models.query import QuerySet

# Create your models here.
class CustomManager(models.Manager):

    def get_queryset(self):

        return super().get_queryset().order_by('eno')

    # def get_emp_sal_range(self, esal1, esal2):

    #     return super().get_queryset().filter(esal__range = (esal1, esal2))
    
    # def get_emp_sorted_by(self, parm):

    #     return super().get_queryset().order_by(parm)

class CustomManager1(models.Manager):

    def get_queryset(self):
        return super().get_queryset().order_by('ename')
    
class CustomManager2(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(esal__gt = 40000)
    

class Employee(models.Model):

    eno = models.IntegerField()
    ename = models.CharField(max_length = 50)
    esal = models.FloatField()
    eaddr = models.CharField(max_length = 100)

    objects = CustomManager()

class ProxyEmployee(Employee):

    objects = CustomManager1()
    class Meta:

        proxy = True

class ProxyEmployee1(Employee):

    objects = CustomManager2()
    class Meta:

        proxy = True


    