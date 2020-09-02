from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('meditations/', views.MeditationList.as_view(), name='meditation_list'),
    path('meditations/<int:pk>', views.MeditationDetail.as_view(),
         name='meditation_detail'),
    path('benefits/', views.BenefitList.as_view(), name='benefit_list'),
    path('benefits/<int:pk>', views.BenefitDetail.as_view(), name='benefit_detail'),
]
