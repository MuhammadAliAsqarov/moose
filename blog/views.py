from django.shortcuts import render, redirect
from .models import Post, Comment, Contact


def home_view(request):
    posts = Post.objects.filter(published_on=True)
    d = {
        'posts': posts
    }
    return render(request, 'index.html', context=d)


def about_view(request):
    return render(request, 'about.html')


def blog_view(request):
    data = request.GET
    cat = data.get('cat',None)
    if cat:
        posts = Post.objects.filter(published_on=True, category_id=cat)
    else:
        posts = Post.objects.filter(published_on=True)
    d = {
        'posts': posts
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
    return render(request, 'contact.html')


def blog_detail_view(request, pk):
    if request.method == 'POST':
        data = request.POST
        comment = Comment.objects.create(post_id=pk, name=data["name"], email=data["email"], message=data["message"])
        comment.save()
        return redirect(f'/blog/{pk}/')
    post = Post.objects.filter(id=pk).first()
    comments = Comment.objects.filter(post_id=pk)
    return render(request, 'blog-single.html', {'post': post, 'comments': comments})
