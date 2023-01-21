from django.db import models
from django.contrib.auth.models import User
import os

class Post(models.Model):
    title = models.CharField(max_length=30) #제목
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField() #내용

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) #서로 다른 위치에 저장해야 시간 단축 가능 / blank=True는 필수 항목이 아니라는 뜻
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True) #작성일
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE) #포스트의 작성자가 데베에서 삭제되면 이 포스트도 같이 삭제

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self): # 확장자
        return self.get_file_name().split('.')[-1]
