from django.urls import path

from . import views

urlpatterns = [
    path('', views.inscription, name='class_add'),
    path('taller_guitarra/', views.ins_TallerGuitarra, name='TallerGuitarra'),
    path('observadores/', views.ins_Observadores, name='Observadores'),
    #path('', views.ClassListView.as_view(), name='enrolled_student'),
    #path('add/', views.ClassCreateView.as_view(), name='class_add'),
    #path('<int:pk>/', views.ClassUpdateView.as_view(), name='class_change'),
    #path('ajax/load-levels/', views.load_levels, name='ajax_load_levels'),
    #path('ajax/load-classes/', views.load_classes, name='ajax_load_classes'),
]