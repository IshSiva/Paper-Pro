from django.db import models
from account.models import Author,Reviewer

# Create your models here.
class Paper(models.Model):
    title=models.CharField(max_length=100)
    field=models.CharField(max_length=100)
    paper=models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, null=True)
    status=models.CharField(max_length=20)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE,null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    commentstoauth = models.CharField(max_length=1000, default='', null=True)
    commentstoedit = models.CharField(max_length=1000, default='', null=True)

