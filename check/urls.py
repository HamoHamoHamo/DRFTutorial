from django.urls import path
from check import views


urlpatterns = [
    path('', views.check),
    # path('csrftoken/', views.EnsureCsrf.as_view(), name="csrf"),
]