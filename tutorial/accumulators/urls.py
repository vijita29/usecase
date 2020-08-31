from django.urls import path
from accumulators import views

urlpatterns = [
    path('/', views.AccumulatorListCreate.as_view()),
    path('/by_member', views.MemberAccumulatorList.as_view()),
    path('/<int:pk>/', views.AccumulatorDetails.as_view()),
]