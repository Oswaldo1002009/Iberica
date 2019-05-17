from django.urls import path

from . import views

urlpatterns = [
    path('', views.inscription, name='class_add'),
    path('interdisciplinario/', views.ins_Inter, name='Interdisciplinario'),
    path('taller_guitarra/', views.ins_TallerGuitarra, name='TallerGuitarra'),
    path('observadores/', views.ins_Observadores, name='Observadores'),
    path('intensivo/', views.ins_Intensivo, name='Intensivo'),
    path('elemental/', views.ins_Elemental, name='Elemental'),
    path('independiente/', views.ins_Independiente, name='Independiente')
    #path('', views.ClassListView.as_view(), name='enrolled_student'),
    #path('add/', views.ClassCreateView.as_view(), name='class_add'),
    #path('<int:pk>/', views.ClassUpdateView.as_view(), name='class_change'),
    #path('ajax/load-levels/', views.load_levels, name='ajax_load_levels'),
    #path('ajax/load-classes/', views.load_classes, name='ajax_load_classes'),
]