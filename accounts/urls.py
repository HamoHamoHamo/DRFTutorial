from django.urls import path
from accounts import views


urlpatterns = [
    path('users/', views.user_list),
    path('profile/', views.user_detail)
    # path('csrftoken/', views.EnsureCsrf.as_view(), name="csrf"),
]