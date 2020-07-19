from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,authenticate

from django.forms.utils import ValidationError
from . import models
from account.models import Author,Reviewer

class PaperUploadForm(forms.ModelForm):
	upload_paper = forms.FileField()
	title =  forms.CharField(max_length=100)
	field = forms.CharField(max_length=100)
	description = forms.CharField(max_length=500)
	

	class Meta:
		model = models.Paper
		fields = ['upload_paper']



class DocumentUpdateForm(forms.ModelForm):
	doc = forms.FileField()


	class Meta:
		model = models.Paper
		fields = ['doc']

class CommentsUploadForm(forms.ModelForm):
	comments=forms.CharField(max_length=1000)

	class Meta:
		model=models.Paper
		fields=['comments']


class AuthorEditForm(forms.ModelForm):
	field = forms.CharField(max_length=100, required=False)
	affliation = forms.CharField(max_length=15, required=False)
	country = forms.CharField(max_length= 100, required=False)
	
	

	class Meta(forms.ModelForm):
		model = models.Author
		fields = ['field', 'affliation', 'country']


class CommentsUploadForm(forms.ModelForm):
	commentstoauth=forms.CharField(max_length=1000)
	commentstoedit=forms.CharField(max_length=1000)

	class Meta:
		model=models.Paper
		fields=['commentstoauth','commentstoedit']

class StatusUploadForm(forms.ModelForm):
	status=forms.CharField(max_length=1000)

	class Meta:
		model=models.Paper
		fields=['status']



		




