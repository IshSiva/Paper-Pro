from django.contrib import admin
from django.urls import include, path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	#author dashboard
	path('authordboard/',views.author_dboard, name='author_details'),
	#reviewer dashboard
	path('reviewdboard/',views.reviewer_dboard, name='reviewer_details'),

	#editor dashboard
	path('editordboard/',views.editor_dboard, name='reviewer_details'),

	#document upload
	path('paperupload/', views.upload_paper, name='paper_upload'),
	path('editauthordetails/', views.editAuthor, name="change_auth_details"),


	#paper update
	path('paperupdate/<int:p_id>', views.update_paper, name='paper_update'),

	#assign reviewer
	path('assign/<int:p_id>/<int:r_id>', views.assign_reviewer, name='assign_reviewer'),

	#get reviewers
	path('getreviewers/<int:p_id>', views.get_reviewer, name='get_reviewer'),

	path('addcomments/<int:p_id>/', views.add_comments, name='comments'),
    path('addstatus/<int:p_id>/', views.add_status, name='status'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)