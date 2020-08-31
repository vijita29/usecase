from django.urls import path
from claims import views

urlpatterns = [
    path('/', views.ClaimListCreate.as_view()),
    path('/filterlist', views.ClaimFilterList.as_view()),
    path('/<int:pk>/', views.ClaimDetail.as_view()),
]