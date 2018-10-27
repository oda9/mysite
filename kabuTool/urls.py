from django.urls import path

from . import views

app_name = 'kabuTool'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', views.store,          name='store'),
]