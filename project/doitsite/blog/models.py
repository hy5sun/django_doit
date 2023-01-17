from django.db import models
import os

class Post(models.Model):
    title = models.CharField(max_length=30) #제목
    content = models.TextField() #내용

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) #서로 다른 위치에 저장해야 시간 단축 가능 / blank=True는 필수 항목이 아니라는 뜻
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True) #작성일
    updated_at = models.DateTimeField(auto_now=True)
    # author

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self): # 확장자
        return self.get_file_name().split('.')[-1]
