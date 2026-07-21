from django.urls import path
from moodspace.views import home, registration, diary, recommendations, favorites, profile, create_diary, edit_diary, delete_diary, vibe_recommendation, remove_favorites, add_status, ReccomendationApi
from django.contrib.auth import views as auth_views
 
urlpatterns = [
    path('', home, name='home'),
    path('register/', registration, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='moodspace/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path ('my_diary/', diary, name='diary'),
    path('my_recommendations/', recommendations, name='recommendations'),
    path('favorites/', favorites, name='favorites'),
    path('profile/', profile, name='profile'),
    path('create_diary/', create_diary, name='create_diary'),
    path('edit_diary/<int:diary_id>/', edit_diary, name='edit_diary'),
    path('delete_diary/<int:diary_id>/', delete_diary, name='delete_diary'),
    path('vibe_rec/<int:vibe_id>/', vibe_recommendation, name='vibe_rec'),
    path('favorites/remove/<int:recommendation_id>/', remove_favorites, name='remove_favorite'),
    path('status/<int:recommendation_id>/<str:status>/', add_status, name='add_status' ),
    path('api/recommendation/', ReccomendationApi.as_view(), name='api_recommendations'),
    ]