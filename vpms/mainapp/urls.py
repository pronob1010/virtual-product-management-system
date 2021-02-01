from django.urls import path,include
from . import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
    #success page will be visit when process valid and authenticated. 
    path('<str:id>/', views.process, name='process'),
]
