from django.urls import path, include
from django.contrib.auth import views 
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),

    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.CustomPasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('create/', views.UserCreateView.as_view(), name="create"),
    path('create/done', views.UserCreateDoneView.as_view(), name='create_done'),
    path('create/complete/<token>/', views.UserCreateCompleteView.as_view(), name='create_complete'),
    path('profile/', views.UserProfileView.as_view(), name="profile"),
    path('change/', views.EmailChangeView.as_view(), name="change"),
]