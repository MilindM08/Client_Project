from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register_client/', views.register_client, name='register_client'),
    path('client_list/', views.client_list, name='client_list'),
    path('client_detail/', views.client_detail, name='client_detail'),
    path('client_edit/', views.client_edit, name='client_edit'),
    path('client_delete/', views.client_delete, name='client_delete'),
    path('add_project/add/', views.add_project, name='add_project'),
    path('assigned_projects/', views.assigned_projects, name='assigned_projects'),
    path('project_list/', views.project_list, name='project_list'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout_view/', views.logout_view, name='logout_view'),
    

]