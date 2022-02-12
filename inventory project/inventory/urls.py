from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomePageListView.as_view(), name = 'index'),
    
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    
    path('logout/', views.LogOutView.as_view(), name = 'logout'),

    path('details/<int:year>/<int:month>/<int:day>/<slug:invent>/', views.inventory_details, name = 'details'),

    path('new/', views.CreateInventoryView.as_view(), name = 'create'),

    path('edit/<slug:slug>/', views.UpdateInventoryView.as_view(), name = 'update'),
]
