from django.urls import path
from . import views

urlpatterns = [
    path('/<int:pk>/', views.PostDetail.as_view()),
    path('/', views.PostList.as_view()),
    #path('/<int:pk>/', views.single_post_page), #상세 페이지 / 정수 값을 pk 변수에 담아 함수로 넘기기
    #path('/', views.index),
]