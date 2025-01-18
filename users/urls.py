from django.urls import path
from users.views import (
  AllUsersView,
  ChangePasswordView,
  PasswordResetView,
  RegisterUserView,
  UserView
)


urlpatterns = [
    path('users/register', RegisterUserView.as_view(), name='register-user'),
    path('users/change_password', ChangePasswordView.as_view(), name='change-password'),
    path('users/reset_password', PasswordResetView.as_view(), name='reset-password'),
    path('users', AllUsersView.as_view(), name='users-list'),
    path('user', UserView.as_view(), name='user-detail')
]
