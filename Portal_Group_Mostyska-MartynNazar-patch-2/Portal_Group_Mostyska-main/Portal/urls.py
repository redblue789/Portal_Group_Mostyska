from django.contrib import admin
from django.urls import path
from GroupPortal import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('forum/', views.forum_list, name='forum_list'),
    path('forum/<int:pk>/', views.forum_detail, name='forum_detail'),
    path('forum/new/', views.create_forum_topic, name='create_forum_topic'),
]