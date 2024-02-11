from django.urls import path
from django.views.generic.base import TemplateView
from .views import createTask,viewTask,deleteTask

urlpatterns = [
    path('create',createTask,name='createTask'),
    path('',viewTask,name='viewTask'),
    path('delete/<int:id>',deleteTask,name='deleteTask'),
    path('contact',TemplateView.as_view(template_name='contact.html'), name='contact')
]