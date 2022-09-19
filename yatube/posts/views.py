from django.shortcuts import render, get_object_or_404
from .models import Post, Group

POSTS_NUMBER = 10  # Кол-во сообщений для вывода на экран


def index(request):
    # в posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию
    posts = Post.objects.select_related('group')[:POSTS_NUMBER]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_NUMBER]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
