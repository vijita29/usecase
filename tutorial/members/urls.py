from django.urls import path
from members import views

urlpatterns = [
    path('/', views.MemberListCreate.as_view()),
    path('/<int:pk>/', views.MemberDetail.as_view()),
]