from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name='main'),
    path("news/", views.NewsPageView.as_view(), name='news'),
    path("courses/", views.CoursesListPageView.as_view(), name='courses'),
    path("contacts/", views.ContactsPageView.as_view(), name='contacts'),
    path("doc_site/", views.DocSitePageView.as_view(), name='docs'),
    path("login/", views.LoginPageView.as_view(), name='login'),
    path("courses/<int:pk>",views.CourseDescriptionView.as_view(), name='CourseDescription'),
    path("news/<int:pk>", views.NewsBodyView.as_view(), name='NewsBody')
]
