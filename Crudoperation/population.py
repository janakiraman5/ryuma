import os
os.environ.setdefault('DJANGO_SETTING_MODULE','Crudoperation.setting')

import django
django.setup()
from faker import Faker

from Crudi.models import *
from random import *
faker = Faker()

def generate(n):
    for i in range(n):
        fsname =faker.name()
        fsclass = randint(1,12)
        Stud_record = Student.object.get_or_create(sname = fsname,sclass = fsclass )    

generate(10)


