import os

from django.shortcuts import render, redirect
from .models import Post, Comment, Contact
from django.core.paginator import Paginator
import requests

BOT_TOKEN =' '
CHAT_ID = ' '


def home_view(request):
    posts = Post.objects.filter(published_on=True).order_by('-views_count')[:2]
    d = {
        'posts': posts,
        'home': 'active'
    }
    return render(request, 'index.html', context=d)


def about_view(request):
    return render(request, 'about.html', context={'about': 'active'})


def blog_view(request):
    data = request.GET
    cat = data.get('cat', None)
    page = data.get('page', 1)
    if cat:
        posts = Post.objects.filter(published_on=True, category_id=cat)
        d = {
            'posts': posts,
            'blog': 'active',

        }
        return render(request, 'blog.html', context=d)
    posts = Post.objects.filter(published_on=True)
    page_obj = Paginator(posts, 2)
    d = {
        'blog': 'active',
        'posts': page_obj.get_page(page)

    }

    return render(request, 'blog.html', context=d)


def contact_view(request):
    if request.method == 'POST':
        data = request.POST
        obj = Contact.objects.create(full_name=data['name'],
                                     email=data['email'],
                                     subject=data['subject'],
                                     message=data['message'])
        obj.save()
        text = f"""
        project: Moose
        id:{obj.id}
        name:{obj.full_name}
        email:{obj.email}
        subject:{obj.subject}
        message:{obj.message}
        timestamp:{obj.created_at}
        """
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}'
        response = requests.get(url)
        print(response)
        return redirect('/contact')
    return render(request, 'contact.html', context={'contact': 'active'})


def blog_detail_view(request, pk):
    if request.method == 'POST':
        data = request.POST
        post = Post.objects.filter(pk=pk).first()
        comment = Comment.objects.create(post_id=pk, name=data["name"], email=data["email"], message=data["message"])
        comment.save()
        post.comments_count += 1
        post.save(update_fields=['comments_count'])
        return redirect(f'/blog/{pk}/')
    post = Post.objects.filter(pk=pk).first()
    post.views_count += 1
    post.save(update_fields=['views_count'])
    comments = Comment.objects.filter(post_id=pk)
    return render(request, 'blog-single.html', {'post': post, 'comments': comments})
