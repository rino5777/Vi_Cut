from django import forms
from .models import VideoForm


class Videof(forms.ModelForm):
    class Meta:
        model = VideoForm

        fields = ('video', )

        