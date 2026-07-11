from django import forms
from moodspace.models import Person
from django.contrib.auth.forms import UserCreationForm
 
class PersonForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Person
        fields = ('username',)