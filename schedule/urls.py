from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClassListView.as_view(), name='enrolled_student'),
    path('add/', views.ClassCreateView.as_view(), name='class_add'),
    path('<int:pk>/', views.ClassUpdateView.as_view(), name='class_change'),
    path('ajax/load-levels/', views.load_levels, name='ajax_load_levels'),
]