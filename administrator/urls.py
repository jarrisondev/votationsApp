from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash, name='dash'),
    path('createUser/', views.createUser, name='createUser'),
    # users
    path('users/', views.users, name='users'),
    path('createUser/', views.createUser, name='createUser'),
    path('updateUser/<int:id>', views.updateUser, name='updateUser'),
    path('deleteUser/<int:id>', views.deleteUser, name='deleteUser'),
]