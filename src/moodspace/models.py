from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Diary(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='diaries')
    text = models.TextField('Текст', blank=True, null=True)
    image_user = models.ImageField(
        'Фото в дневнике',
        upload_to='diary_photos/',
        blank=True,
        null=True
    )
    
    date_created = models.DateTimeField('Дата записи', auto_now_add=True)
   
    class Meta:
        verbose_name = 'Запись дневника'
        verbose_name_plural = 'Записи дневника'


    def __str__(self):
        return self.text[:20] if self.text else 'Нет записей'



class Vibe(models.Model):
    
    vibe_name = models.CharField('Название настроения', max_length=255)
    image_vibe = models.CharField('Стикер', max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = 'Настроение'

    def __str__(self):
        return self.vibe_name

class Recommendation(models.Model):

    class RecommenationType(models.TextChoices):
        MOVIE = 'movie', 'Фильм'
        SERIES = 'series', 'Сериал' 
        BOOK = 'book', 'Книга'
        GAME = 'game', 'Игра'
        FACT = 'fact', 'Интересный факт'
    
    type_rec = models.CharField('Тип рекомендации', max_length=100, choices=RecommenationType.choices)
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    image_rec = models.CharField('Изображение рекомендации', blank=True, null=True)
    vibe = models.ForeignKey(Vibe, null=True, on_delete=models.SET_NULL, related_name='recommendations')

    class Meta:
        verbose_name = 'Рекомендация'
        verbose_name_plural = 'Рекомендации'

    def __str__(self):

        return f'{self.type_rec}:{self.title}'
        

class RecommendUser(models.Model):

    class RecommendationStatus(models.TextChoices):
        FAVORITE = 'favorite', 'Избранное'
        VIEWED = 'viewed', 'Просмотрено'
        DISLIKED = 'disliked', 'Не понравилось'

    user = models.ForeignKey(
        Person,
        null = True,
        on_delete=models.SET_NULL,
        related_name='recommendations'
    )

    recommendation = models.ForeignKey(
        Recommendation,
        null = True,
        on_delete=models.SET_NULL,
        related_name='user_links'
    )

    status_rec = models.CharField('Статус', max_length=100, choices=RecommendationStatus.choices)

    class Meta:
        verbose_name = 'Рекомендация пользователя'
        verbose_name_plural = 'Рекомендации пользователя'

    def __str__(self):

        return self.status_rec
    
class MoodEntry(models.Model):
    user = models.ForeignKey(
        Person,
        null = True,
        on_delete=models.SET_NULL,
        related_name='mood_entries'

    )

    vibe_user = models.ForeignKey(
        Vibe,
        null = True,
        on_delete=models.SET_NULL,
        related_name='mood_vibe'
    )

    created_date = models.DateTimeField('Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Выбранное настроение'
        verbose_name_plural = 'Выбранные настроения'

    def __str__(self):

        return f'{self.user}: {self.vibe_user}'
