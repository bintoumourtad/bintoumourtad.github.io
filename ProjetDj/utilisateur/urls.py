from django.urls import path
from .views import LoginPage,Signup
from django.contrib.auth.views import LogoutView



urlpatterns = [
        path('login/', LoginPage, name='login'),
        path('Signup/', Signup, name='signup'),
        path('logout/',LogoutView.as_view(), name='logout'),




]
