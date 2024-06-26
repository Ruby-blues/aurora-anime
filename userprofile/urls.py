from django.urls import path
from . import views


urlpatterns = [
    path('', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('edit', views.UpdateUserView.as_view(), name='edit'),
]
