from django import forms
from django.forms import ModelForm, Textarea,TextInput
from scrapper.models import *
class UploadForm(forms.ModelForm):
	class Meta:
		model=Uploaded_file
		exclude=()
	
