from django.db import models
from datetime import datetime

class News(models.Model):
    title=models.CharField(max_length=255,verbose_name="Head")
    anons=models.CharField(max_length=255,verbose_name="Anons")
    content=models.TextField(blank=True,null=True,verbose_name="News full text")
    content_markdown=models.BooleanField(default=False, verbose_name="As markdown")
    created_at=models.DateTimeField(auto_now_add=datetime.now(), editable=False)
    updated_at=models.DateTimeField(auto_now=datetime.now(), editable=False)
    deleted=models.BooleanField(default=False)

    def delete(self):
        self.deleted=True
        self.save()


class Courses(models.Model):
    title=models.CharField(max_length=255,verbose_name="Name of course")
    description=models.TextField(blank=True,null=True,verbose_name="Description")
    cost=models.PositiveIntegerField(verbose_name="cost")
    hours=models.PositiveSmallIntegerField(verbose_name="Hours")
    lessons_num=models.PositiveSmallIntegerField(verbose_name="Hours")
    tasks=models.PositiveSmallIntegerField(verbose_name="Hours")
    created_at=models.DateTimeField(auto_now_add=datetime.now(), editable=False)
    updated_at=models.DateTimeField(auto_now=datetime.now(), editable=False)
    deleted=models.BooleanField(default=False)

    def delete(self):
        self.deleted=True
        self.save()


class Lessons(models.Model):
    title=models.CharField(max_length=255,verbose_name="Name of course")
    description=models.TextField(blank=True,null=True,verbose_name="Description")
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    num=models.PositiveSmallIntegerField(verbose_name="Number of lesson")
    tasks=models.PositiveSmallIntegerField(verbose_name="Hours")
    created_at=models.DateTimeField(auto_now_add=datetime.now(), editable=False)
    updated_at=models.DateTimeField(auto_now=datetime.now(), editable=False)
    deleted=models.BooleanField(default=False)

    def delete(self):
        self.deleted=True
        self.save()

class Teachers(models.Model):
    surname=models.CharField(max_length=255,verbose_name="Name")
    name=models.CharField(max_length=255,verbose_name="Surname")
    email=models.EmailField()
    phone=models.PositiveSmallIntegerField()
    course=models.ManyToManyField(Courses)
    created_at=models.DateTimeField(auto_now_add=datetime.now(), editable=False)
    updated_at=models.DateTimeField(auto_now=datetime.now(), editable=False)
    deleted=models.BooleanField(default=False)

    def delete(self):
        self.deleted=True
        self.save()