from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
	path('', views.index, name='index'),
    path('videos/', views.videos, name='videos'),
    path('contato/', views.contato, name='contato'),
]