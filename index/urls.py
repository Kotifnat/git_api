from django.urls import path
from index import views

urlpatterns = [
    path('', views.reps, name='reps'),
    path('<str:repo/', views.rep_detail, name='rep_detail'),
    ]
