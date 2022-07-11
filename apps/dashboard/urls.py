from django.urls import path

from .views import dashborad

urlpatterns = [
    path('', dashborad, name='dashborad'),
]
