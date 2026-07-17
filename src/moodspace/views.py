from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PersonForm, DiaryForm
from .models import Diary, Vibe, Recommendation, RecommendUser, MoodEntry
from random import choice
from django.db.models import Count

def home(request):
    return render (request, 'moodspace/home.html')

def registration(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PersonForm()
    
    return render(request, 'moodspace/register.html', {'form': form})


@login_required
def create_diary(request):

    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)

        if form.is_valid():
            diary = form.save(commit=False)
            diary.user = request.user
            diary.save()

            return redirect('diary')
        
    else:
        form = DiaryForm()

    return render(request, 'moodspace/create_diary.html', {'form': form})

@login_required
def diary(request):

    diaries = Diary.objects.filter(user=request.user)
    selected_date = request.GET.get('date')
    
    if selected_date:
        diaries = diaries.filter(date_created__date = selected_date)
    
    diaries = diaries.order_by('-date_created')
    return render(request, 'moodspace/diary.html', {'diaries': diaries})


@login_required
def edit_diary(request, diary_id):

    diary = Diary.objects.get(id=diary_id, user=request.user)

    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES, instance=diary)

        if form.is_valid():
            form.save()

            return redirect('diary')
        
    else:
        form = DiaryForm(instance=diary)

    return render(request, 'moodspace/edit_diary.html', {'form': form})


@login_required
def delete_diary(request, diary_id):

    diary = Diary.objects.get(id=diary_id, user=request.user)

    if request.method == 'POST':
        diary.delete()
        return redirect('diary')



def recommendations(request):
    
    vibes = Vibe.objects.all()
    return render(request, 'moodspace/recommendations.html', {'vibes': vibes})


def vibe_recommendation(request, vibe_id):

    vibe = get_object_or_404(Vibe, id=vibe_id)


    if request.user.is_authenticated:
        MoodEntry.objects.create(user=request.user, vibe_user=vibe,)

    cards=[]

    for i in Recommendation.RecommenationType.values:
        recommendations = Recommendation.objects.filter(vibe=vibe, type_rec = i,)


        if recommendations.exists():
            cards.append(choice(list(recommendations)))


    return render(request, 'moodspace/vibe_rec.html', {'vibe': vibe, 'cards':cards},)


    
@login_required
def add_status(request, recommendation_id, status):
    recommendation = get_object_or_404(Recommendation, id=recommendation_id)
    
    if status not in RecommendUser.RecommendationStatus.values:
        return redirect('recommendations')

    RecommendUser.objects.update_or_create(
        user=request.user,
        recommendation=recommendation,
        defaults={'status_rec': status}
    ) 
    
    return redirect(request.META.get('HTTP_REFERER', 'recommendations'))    

@login_required
def favorites(request):
    favorites = RecommendUser.objects.filter(user = request.user,
    status_rec= RecommendUser.RecommendationStatus.FAVORITE).select_related('recommendation') 
    return render(request, 'moodspace/favorites.html', {'favorites': favorites},)

@login_required
def remove_favorites(request, recommendation_id):
    favorite = get_object_or_404(
        RecommendUser,
        user=request.user,
        recommendation_id=recommendation_id,
        status_rec=RecommendUser.RecommendationStatus.FAVORITE,
    )

    favorite.delete()

    return redirect('favorites')

@login_required
def profile(request):

    status = request.GET.get('status', 'all')

    recommendations = RecommendUser.objects.filter(user=request.user).select_related('recommendation')

    if status == 'viewed':
        recommendations = recommendations.filter(status_rec=RecommendUser.RecommendationStatus.VIEWED)

    elif status == 'disliked':
        recommendations = recommendations.filter(status_rec = RecommendUser.RecommendationStatus.DISLIKED)

    elif status == 'favorite':
        recommendations = recommendations.filter(status_rec = RecommendUser.RecommendationStatus.FAVORITE)

    statistic = (
        MoodEntry.objects.filter(user=request.user).values('vibe_user__vibe_name')
        .annotate(total=Count('id')).order_by('-total')
    )
    diary_count = Diary.objects.filter(user=request.user).count()


    return render(request, 'moodspace/profile.html', {'recommendations': recommendations, 'statistic':statistic, 'status': status, 'diary_count': diary_count})
