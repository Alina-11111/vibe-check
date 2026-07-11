from django.urls import path
from moodspace.views import home, registration
from django.contrib.auth import views as auth_views
 
urlpatterns = [
    path('/', home, name='home'),
    path('register/', registration, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='moodspace/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    ]