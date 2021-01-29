from django.urls import path, re_path
from .views import (
    AccountLoginView, 
    AccountLogoutView, 
    AccountPasswordChangeView, 
    AccountPasswordChangeDoneView,
    AccountPasswordResetView,
    AccountPasswordResetDoneView,
    AccountPasswordResetConfirmView,
    AccountPasswordResetCompleteView,
    DashboardView,
    #profile,
)

app_name = 'account'

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('password-change/', AccountPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', AccountPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', AccountPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', AccountPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', AccountPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', AccountPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #path('profile/', profile, name='profile'),
    path('', DashboardView.as_view(), name='dashboard'),
]