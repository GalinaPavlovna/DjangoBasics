# Generated by Django 3.2 on 2023-02-20 18:20

from django.db import migrations
from random import randrange


def creation_courses(app,se):
    Courses=app.get_model('mainapp','Courses')
    with open('/home/galka/Desktop/DjangoBasics/BraniacLMS/mainapp/documents/courses', encoding='utf-8') as f:
        a=f.readline()
        while a!='end':
            ttl=a
            d=f.readline()
            dscr=''
            while d!='\n':
                dscr+=d.strip()
                d=f.readline()
            a=f.readline().strip()
            Courses.objects.update_or_create(
                title=ttl,
                description=dscr,
                cost=randrange(10,100)*100,
                hours=randrange(20,40),
                lessons_num=randrange(10,25),
                tasks=randrange(25,50)
            )

    
class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [migrations.RunPython(creation_courses)]
