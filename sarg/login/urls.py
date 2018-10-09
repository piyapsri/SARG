from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.homeCarroussel, name='index2'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register/', views.register, name='register'),
# Reet password
#    path('resetpassword/passwordsent/', 'auth.views.password_reset_done'),
#    path('resetpassword/', 'auth.views.password_reset'),
#    path('reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/', 'auth.views.password_reset_confirm'),
#    path('reset/done/', 'auth.views.password_reset_complete'),
]
