from django.urls import path
from maps import views

urlpatterns = [
    path('', views.MapHome.as_view(), name='map_list'),
    path('<int:pk>/', views.MapDetailView.as_view(), name='map_detail'),
    path('add/', views.AddNewMap.as_view(), name='add_map'),
    path('delete/<pk>/', views.delete_map, name='delete_map'),
]