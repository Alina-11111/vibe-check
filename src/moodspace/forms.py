from django import forms
from moodspace.models import Person, Diary
from django.contrib.auth.forms import UserCreationForm
 
class PersonForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Person
        fields = ('username',)


class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('text', 'image_user')


        
        