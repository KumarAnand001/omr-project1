from django.contrib import admin
from myApp.models import Employee, ProxyEmployee, ProxyEmployee1

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):

    list_display = ['eno', 'ename', 'esal', 'eaddr']

class ProxyEmployeeAdmin(admin.ModelAdmin):

    list_display = ['eno', 'ename', 'esal', 'eaddr']

class ProxyEmployeeAdmin1(admin.ModelAdmin):

    list_display = ['eno', 'ename', 'esal', 'eaddr']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ProxyEmployee, ProxyEmployeeAdmin)
admin.site.register(ProxyEmployee1, ProxyEmployeeAdmin1)
