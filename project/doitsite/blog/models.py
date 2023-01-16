from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30) #제목
    content = models.TextField() #내용

    created_at = models.DateTimeField(auto_now_add=True) #작성일
    updated_at = models.DateTimeField(auto_now=True)
    # author

    def __str__(self):
        return f'[{self.pk}] {self.title}'
