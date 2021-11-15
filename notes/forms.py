from django.forms import ModelForm
from .models import Note

class NoteFrom(ModelForm):
    class Meta:
        model = Note
        fields = ['title','content','importance']