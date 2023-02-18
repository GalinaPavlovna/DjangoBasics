from django.views.generic import TemplateView
from datetime import datetime
from random import choice


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
        lst="водопроводе газопроводе электрической_подстанции крыше_дома ушах мозге".split()
        context = super().get_context_data(**kwargs)
        context['my_title']='News of Braniac'
        context ['range']=range(5)
        context ["news_date"]=datetime.now()
        context["word"]=choice(lst)
        return context

class NewsPaginatorView(NewsPageView):

    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page']=page
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
        context['my_title']='Braniac courses'
        return context


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_title']='Braniac contacts '
        return context
