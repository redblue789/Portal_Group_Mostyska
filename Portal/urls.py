from django.contrib import admin
from django.urls import path
from GroupPortal import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Форум відкривається і на головній, і за адресою /forum/
    path('', views.forum_list, name='home'),
    path('forum/', views.forum_list, name='forum_list'),
    path('forum/<int:pk>/', views.forum_detail, name='forum_detail'),
    path('forum/new/', views.create_forum_topic, name='create_forum_topic'),
]