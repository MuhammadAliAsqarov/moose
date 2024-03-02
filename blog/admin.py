from django.contrib import admin
from .models import Post, Comment, Contact, Category


#class CategoryAdmin(admin.ModelAdmin):
    #list_display = ('name', 'created_at')


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'author','view_count', 'published_on', 'created_at')
    list_display_links = ['id', 'title']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')

class ContactAdmin(admin.ModelAdmin):
        list_display = ('id', 'full_name', 'solved', 'created_at')
        list_display_links = ['id', 'full_name']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)
