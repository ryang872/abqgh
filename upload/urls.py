from django.urls import path
from . import views

urlpatterns = [
    # path('', views.HomePageView.as_view(), name='home'),
    # path('tiplist/', views.TipListView.as_view(), name='tip_list'),
    # path('tiplist/add/', views.UploadTipView.as_view(), name='add_tip'),
    # path('detail/<pk>/', views.TipDetailView.as_view(), name='tip_detail'),
    # path('delete/<pk>/', views.delete_person, name='delete_person'),
    path('', views.TipListView.as_view(), name='tip_list'),
    path('<int:pk>/', views.TipDetailView.as_view(), name='tip_detail'),
    path('add/', views.UploadTipView.as_view(), name='add_tip'),
    path('delete/<pk>/', views.delete_person, name='delete_person'),
]