from django.urls import path
from check import views


urlpatterns = [
    path('', views.check),
    path('monthly/<str:month>', views.AttendanceListAPIView.as_view()),
    path('profile/', views.profile),
    path('<int:pk>/', views.AttendanceDestroyAPIView.as_view()),
    # path('csrftoken/', views.EnsureCsrf.as_view(), name="csrf"),
]