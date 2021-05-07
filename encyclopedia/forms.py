from django import forms
from django.forms import Textarea

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    content = forms.CharField(widget=forms.Textarea(attrs={"style": "height:500px; width:1000px"}),label='')

    def editContent(self):
        content = forms.CharField(widget=forms.Textarea(attrs={"style": "height:500px; width:1000px"}),label='')
        return content