from django.contrib import admin
from .models import Person, Diary, Vibe, Recommendation, RecommendUser, MoodEntry
from django.contrib.auth.admin import UserAdmin
 
@admin.register(Person)
class PersonAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username','email', 'first_name', 'last_name')
    
@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'image_user', 'date_created')
    list_filter = ('date_created',)
 
@admin.register(Vibe)
class VibeAdmin(admin.ModelAdmin):
    list_display = ('vibe_name', 'image_vibe')
    search_fields = ('vibe_name',)
    
@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('type_rec', 'title', 'image_rec', 'vibe')
    search_fields = ('title', 'description')
    list_filter = ('type_rec', 'vibe')
    
    
@admin.register(RecommendUser)
class RecommendUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'recommendation', 'status_rec')
    list_filter = ('status_rec',)
    search_fields = ('user__username', 'recommendation__title')
 
@admin.register(MoodEntry)
class MoodEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'vibe_user', 'created_date')  
    list_filter = ('created_date', 'vibe_user')

# Register your models here.
