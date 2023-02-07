from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True) # 카테고리 이름 / unique=True: 동일한 name을 갖는 카테고리를 만들 수 없다.
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True) # slugField : 사람이 읽을 수 있는 텍스트. 고유 URL을 만들고 싶을 때 주로 사용.
    # 카테고리는 포스트만큼 개수가 많지 않기 때문에 사람이 읽고 그 뜻을 알 수 있게 고유 URL을 사용한다.
    # allow_unicode=True : 한글도 사용 가능

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'
    
    class Meta: #복수형 직접 입력
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=30) #제목
    hook_text = models.CharField(max_length=100, blank=True)
    content = MarkdownxField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) #서로 다른 위치에 저장해야 시간 단축 가능 / blank=True는 필수 항목이 아니라는 뜻
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True) #작성일
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) #포스트의 작성자가 데베에서 삭제되면 작성자명을 빈칸으로 둔다

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self): # 확장자
        return self.get_file_name().split('.')[-1]

    def get_content_markdown(self):
        return markdown(self.content)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 처음 생성될 때 시간 저장
    modified_at = models.DateTimeField(auto_now=True) # 저장할 때 시간 저장

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return f'https://doitdjango.com/avatar/id/1447/5b269ebf572b5c5e/svg/{self.author.email}'
