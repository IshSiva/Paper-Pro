from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,authenticate

from django.forms.utils import ValidationError

from . import models



User=get_user_model()

class AuthorRegistrationForm(forms.ModelForm):

	#the additional fields that are required for a pgr are defined here so that they can be used in the form
	email = forms.CharField(max_length=100, required=True)
	
	contact = forms.CharField(max_length=15, required=True)
	field = forms.CharField(max_length= 100, required=True)
	affliation = forms.CharField(max_length= 100, required=True)
	country = forms.CharField(max_length= 100)
	

	password1 = forms.CharField(label= 'Password', widget=forms.PasswordInput, required=True, min_length=8)
	password2 = forms.CharField(label= 'Confirm Password', widget=forms.PasswordInput, required=True, min_length=8)

	#to check for unique email constraint
	def clean_email(self):
		email = self.cleaned_data['email']
		User = get_user_model()
		qs = User.objects.filter(email = email)
		if qs.exists():
			raise forms.ValidationError("Email exists")
		return email


	#to validate whether both the passwords are the same
	def clean_password2(self):

		password1 = self.cleaned_data['password1']
		password2 = self.cleaned_data['password2']
		if (password1 and password2) and (password1!=password2):
			raise forms.ValidationError("Passwords don't match")
		return password2




    
    
	class Meta(forms.ModelForm):
		model = get_user_model() 
		fields = ['email', 'username','first_name','last_name','password1','password2', 'field', 'affliation','contact', 'country']


	#saving the form. Here we first save the user and then save the pgr
	def save(self):
		#print("hello")
		user= super().save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.contact = self.cleaned_data['contact']
		
		user.set_password(self.cleaned_data['password1'])
		user.isauthor = True
		
		user.save()

		author = models.Author.objects.create(user=user) #we assign the user to the pgr
		
		
		author.field = self.cleaned_data['field']
		author.affliation= self.cleaned_data['affliation']
		author.country = self.cleaned_data['country']
		
		#print(pgr.profile_pic)
		author.save()

		return user


class ReviewerRegistrationForm(forms.ModelForm):

	#the additional fields that are required for a pgr are defined here so that they can be used in the form
	email = forms.CharField(max_length=100, required=True)
	
	contact = forms.CharField(max_length=15, required=True)
	field = forms.CharField(max_length= 100, required=True)
	

	password1 = forms.CharField(label= 'Password', widget=forms.PasswordInput, required=True, min_length=8)
	password2 = forms.CharField(label= 'Confirm Password', widget=forms.PasswordInput, required=True, min_length=8)

	#to check for unique email constraint
	def clean_email(self):
		email = self.cleaned_data['email']
		User = get_user_model()
		qs = User.objects.filter(email = email)
		if qs.exists():
			raise forms.ValidationError("Email exists")
		return email


	#to validate whether both the passwords are the same
	def clean_password2(self):

		password1 = self.cleaned_data['password1']
		password2 = self.cleaned_data['password2']
		if (password1 and password2) and (password1!=password2):
			raise forms.ValidationError("Passwords don't match")
		return password2




    
    
	class Meta(forms.ModelForm):
		model = get_user_model() 
		fields = ['email', 'username','first_name','last_name','password1','password2', 'field', 'contact']


	#saving the form. Here we first save the user and then save the pgr
	def save(self):
		#print("hello")
		user= super().save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']

		user.set_password(self.cleaned_data['password1'])
		user.isreviewer = True
		user.contact = self.cleaned_data['contact']
		
		user.save()

		rev = models.Author.objects.create(user=user) #we assign the user to the pgr
		
		
		rev.field = self.cleaned_data['field']
		
		#print(pgr.profile_pic)
		rev.save()

		return user


User=get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Invalid credentials!')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


