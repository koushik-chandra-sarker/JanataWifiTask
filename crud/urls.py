from django.urls import path

from crud import views

urlpatterns = [
    path('', views.Index),
    path('saveInstance/', views.saveInstance),
    path('deleteInstance/<int:pk>/', views.deleteInstance),
]
