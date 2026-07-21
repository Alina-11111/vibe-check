from django import forms
from moodspace.models import Person, Diary
from django.contrib.auth.forms import UserCreationForm
 
class PersonForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Person
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class']='form-control'

            

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('text', 'image_user')

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placehoder': 'Запиши воспоминание...'
            }),
            'image_user': forms.ClearableFileInput(attrs={
                'class': 'form_control'
            })
        }



    
        