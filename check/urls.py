from django.urls import path
from check import views


urlpatterns = [
    path('', views.check),
    path('list/', views.AttendanceListAPIView.as_view()),
    path('profile/', views.profile),
    # path('csrftoken/', views.EnsureCsrf.as_view(), name="csrf"),
]