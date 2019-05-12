from django.urls import path

from userprofile import views

urlpatterns = [
    path('', views.index, name='profileform'),
    #path('form/', views.CreateProfile.as_view(), name='userprofile'),
    path('form/', views.profile, name='userprofile'),
    #path('<int:pk>/', views.ClassUpdateView.as_view(), name='class_change'),
]