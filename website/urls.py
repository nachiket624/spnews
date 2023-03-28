from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('news/<int:id>/',views.news,name="news")
]