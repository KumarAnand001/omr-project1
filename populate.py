import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ormProject1.settings')
import django
django.setup()

from myApp.models import Employee
from random import randint

from myApp.models import Employee
from faker import Faker
from random import randint

fake = Faker()

def populate(n):

    for i in range(n):

        feno = randint(1001, 9999)
        fename = fake.name()
        fesal = randint(20000, 80000)
        feaddr = fake.city()

        emp_record = Employee.objects.get_or_create(eno = feno, ename = fename, esal = fesal, eaddr = feaddr)

populate(20)