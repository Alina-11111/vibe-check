from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PersonForm, DiaryForm
from .models import Diary
from django.utils import timezone

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
    return render(request, 'moodspace/recommendations.html')



@login_required
def favorites(request):
    return render(request, 'moodspace/favorites.html')


@login_required
def profile(request):
    return render(request, 'moodspace/profile.html')