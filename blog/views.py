from django.shortcuts import render, redirect
from .models import Post, Comment, Contact
from django.core.paginator import Paginator
import requests


def home_view(request):
    posts = Post.objects.filter(published_on=True).order_by('-view_count')[:2]
    d = {
        'posts': posts,
        'home': 'active'
    }
    return render(request, 'index.html', context=d)


def about_view(request):
    return render(request, 'about.html', context={'about':'active'})


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
        return redirect('/contact')
    return render(request, 'contact.html', context={'contact': 'active'})


def blog_detail_view(request, pk):
    if request.method == 'POST':
        data = request.POST
        comment = Comment.objects.create(post_id=pk, name=data["name"], email=data["email"], message=data["message"])
        comment.save()
        return redirect(f'/blog/{pk}/')
    post = Post.objects.filter(id=pk).first()
    post.view_count += 1
    post.save(update_fields=['view_count'])
    comments = Comment.objects.filter(post_id=pk)
    return render(request, 'blog-single.html', {'post': post, 'comments': comments})
