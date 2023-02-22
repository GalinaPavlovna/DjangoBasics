from django.views.generic import TemplateView
from datetime import datetime
import mainapp
from random import choice
from django.shortcuts import get_object_or_404


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_title']='Welcome to Braniac!'
        return context


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_title']='News of Braniac'
        context['news_lst']=mainapp.models.News.objects.all()[:5]
        return context

class NewsPaginatorView(NewsPageView):

    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page']=page
        return context

class NewsBodyView(TemplateView):
    template_name = "mainapp/news_body.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_obj']=get_object_or_404(mainapp.models.News, pk=pk)
        return context

class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_title']='Braniac - documents'
        return context


class CoursesListPageView(TemplateView):
    template_name = "mainapp/courses_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses_lst']=mainapp.models.Courses.objects.all()
        context['my_title']='Braniac courses'
        return context

class CourseDescriptionView(TemplateView):
    template_name = "mainapp/Course_description.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_obj']=get_object_or_404(mainapp.models.Courses, pk=pk)
        context['my_title']=context['course_obj'].title
        context['teachers']=mainapp.models.Teachers.objects.filter(course=context['course_obj'])
        context['lessons']=mainapp.models.Lessons.objects.filter(course=context['course_obj'])
        return context

 

class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_title']='Braniac contacts '
        return context
