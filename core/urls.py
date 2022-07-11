from re import template
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from apps.main.views import frontpage, signup

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('app/', include('apps.dashboard.urls')),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
