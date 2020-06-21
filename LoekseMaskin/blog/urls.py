from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='blogg.html'), name='blogg'),
    path('<int:number>', views.index, name='blogIndex'),
]
