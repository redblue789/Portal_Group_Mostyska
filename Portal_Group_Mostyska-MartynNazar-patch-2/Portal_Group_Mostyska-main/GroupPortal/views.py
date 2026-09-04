from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import ForumTopic, ForumPost
from .forms import ForumTopicForm, ForumPostForm


def index(request):
    return render(request, 'forum/index.html')


def is_staff_or_moderator(user):
    return user.is_staff or user.groups.filter(name='Moderators').exists()


def forum_list(request):
    topics = ForumTopic.objects.all().order_by('-created_at')
    return render(request, 'forum/forum_list.html', {'topics': topics})


def forum_detail(request, pk):
    topic = get_object_or_404(ForumTopic, pk=pk)
    posts = topic.posts.all().order_by('created_at')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.author = request.user
            post.save()
            return redirect('forum_detail', pk=pk)
    else:
        form = ForumPostForm()

    return render(request, 'forum/forum_detail.html', {'topic': topic, 'posts': posts, 'form': form})


@user_passes_test(is_staff_or_moderator)
def create_forum_topic(request):
    if request.method == 'POST':
        form = ForumTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.created_by = request.user
            topic.save()
            return redirect('forum_list')
    else:
        form = ForumTopicForm()
    return render(request, 'forum/forum_topic_form.html', {'form': form})