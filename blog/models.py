from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/')
    content = models.TextField()
    author = models.CharField(max_length=150)
    author_job = models.CharField(max_length=200, blank=True, null=True)
    author_image = models.ImageField(upload_to='authors/')

    comments_count = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    published_on = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    solved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'name: {self.full_name},  solved: {self.solved}'


class Comment(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    published_on = models.BooleanField(default=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} --- {self.email}'
