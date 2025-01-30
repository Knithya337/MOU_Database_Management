from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('admin_mou/', views.admin_mou, name='admin_mou'),
    path('admin_progress/', views.admin_progress, name='admin_progress'),
    path('admin_report/', views.admin_report, name='admin_report'),
    path('admin_report/', views.admin_report, name='admin_report'),
    path('admin_activity/', views.admin_activity, name='admin_activity'),
    path('admin_expired/', views.admin_expired, name='admin_expired'),
    path('admin_renewal/', views.admin_renewal, name='admin_renewal'),
    
    #path('employee/', views.employee, name='employee'),
    path('mou/', views.admin_mou, name='admin_mou'),
    path('create_mou/', views.create_mou, name='create_mou'),
    path('cancel_url/', views.cancel_url, name='cancel_url'),
    path('success/', views.success_url, name='success_url'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/', views.profile_view, name='profile_view'),
    path('mou_list/', views.mou_list, name='mou_list'),


    #customer
    path('customer/', views.customer, name='customer'),
    path('customer_mou/', views.customer_mou, name='customer_mou'),
    path('customer_progress/', views.customer_progress, name='customer_progress'),
    path('customer_report/', views.customer_report, name='customer_report'),
    
]