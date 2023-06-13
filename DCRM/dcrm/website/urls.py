from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_records, name='record'),
    path('delete_record/<int:pk>', views.delete_records, name='delete_record')
]
