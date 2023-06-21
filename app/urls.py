from django.urls import path, include
from rest_framework import routers

from . import views

routers = routers.DefaultRouter()
routers.register(r'question', views.QuestionView)
routers.register(r'choice', views.ChoiceView)


urlpatterns = [
    path('', include(routers.urls)),
]
