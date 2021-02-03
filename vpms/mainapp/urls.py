from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('success/', views.success, name='success'),
    #success page will be visit when process valid and authenticated. 
    path('<str:id>/', views.process, name='process'),
]
