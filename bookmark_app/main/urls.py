from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.loginPage, name='login'),
  path('logout/', views.logoutUser, name='logout'),
  
  path('', views.overview, name="overview"),
  path('add/', views.add, name='add-bookmark'),
  path('edit/<int:id>', views.update, name='edit-bookmark'),
  path('delete/<int:id>', views.delete, name='delete-bookmark'),
  path('add_tag/', views.add_tag, name='add_tag')
]