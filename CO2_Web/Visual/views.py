from django.shortcuts import render
from django.urls import path
from django.views.generic import TemplateView

app_name = 'Visual'
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]

def index(request):
    return render(request, 'index.html')
