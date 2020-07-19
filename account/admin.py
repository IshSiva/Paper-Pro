from django.contrib import admin
from django import forms
from .models import Author,Reviewer,Editor,User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


admin.site.register(Author)
admin.site.register(Reviewer)
admin.site.register(Editor)

# Register your models here.

#creating a custom user addition form for reviewer

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('isreviewer', 'iseditor','contact')}),
    )

admin.site.register(User, MyUserAdmin)