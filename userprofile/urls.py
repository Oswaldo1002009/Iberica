from django.urls import path

from userprofile import views

urlpatterns = [
    path('', views.index, name='userprofile'),
    #path('form/', views.CreateProfile.as_view(), name='profileform'),
    path('form/', views.profile, name='profileform'),
    #path('<int:pk>/', views.ClassUpdateView.as_view(), name='class_change'),
]