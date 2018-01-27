from django import forms

from music.models import Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            "job_title",
            "tag_name",
            "audio_file",
        ]