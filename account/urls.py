from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from .import views
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns = [
   

    #logging a user in
    path('', views.homepage, name="index"),
    path('login/', views.user_login, name="user_login"),
    path('signup/', views.registerAuthor, name='login_signup_choice'),
    path('password/reset/',PasswordResetView.as_view(template_name='account/password_reset_form.html'),name='password_reset'),

    #password reset done
    path('password/reset/done',PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),name='password_reset_done'),

    #password reset confirm
	path('password/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),name='password_reset_confirm'),

    #password reset complete
    path('reset/done',PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),name='password_reset_complete'),

    #creating a new pgr
   
    
    #to logout the user
    path('logout/', views.user_logout, name="user_logout"),
	
	



 ]