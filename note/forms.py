from django import forms
from .models import Note


class NoteForm(forms.Form):
    # file = forms.FileField()
    #
    # class Meta:
    #     model = Note
    #     fields = ('title', 'description')
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    docfile = forms.FileField(
        label='Select a file'
    )