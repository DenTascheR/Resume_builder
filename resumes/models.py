from django.db import models
from django.conf import settings

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Section(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=255)
    content = models.TextField()

class File(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='resume_files/')
