from django.urls import path
from gatecode import views



urlpatterns = [
    path('', views.GateCodeHome.as_view(), name='gate_list'),
    path('<int:pk>/', views.GateDetailView.as_view(), name='gate_detail'),
    path('add/', views.AddNewCode.as_view(), name='add_gate'),
    path('delete/<pk>/', views.delete_gate, name='delete_gate'),
]