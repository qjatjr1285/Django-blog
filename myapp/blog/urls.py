from django.urls import path
from . import views
# from blog.views import Index

app_name = 'blog'

urlpatterns = [
    # 글 목록 조회
    path("", views.Index.as_view(), name='list'),
    # 글 상세 조회
    path("<int:pk>/", views.DetailView.as_view(), name='detail'), 
    # 글 작성
    path("write/", views.Write.as_view(), name='write'), 
    # 글 수정
    path("edit/<int:pk>/", views.Update.as_view(), name='edit'),
    # 글 삭제
    path("delete/<int:pk>/", views.Delete.as_view(), name='delete'),
    # 코멘트 작성
    path("<int:pk>/comment/write", views.CommentWrite.as_view(), name='cm-write'),
    # 코멘트 삭제
    path("<int:pk>/comment/delete", views.CommentDelete.as_view(), name='cm-delete'),
    # 태그 작성
    path("<int:pk>/hashtag/write", views.HashTagWrite.as_view(), name='tag-write'),
    # 태그 삭제
    path("hashtag/<int:pk>/delete", views.HashTagDelete.as_view(), name='tag-delete'),

]