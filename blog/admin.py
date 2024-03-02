from django.contrib import admin
from .models import Post, Comment, Contact, Category
from datetime import datetime
from django.utils.html import format_html


class PostInline(admin.TabularInline):
    model = Post
    extra = 0
    fields = ('title', 'published_on')


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')
    inlines = (PostInline,)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image','preview_image', 'author', 'view_count', 'published_on', 'created_at')
    list_display_links = ('id', 'title')
    inlines = (CommentInline,)
    search_fields = ('title','author')
    list_filter = ('published_on','author')
    def preview_image(self,obj):
        return format_html("<img height=70 src={}>",obj.image.url)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'solved', 'days', 'created_at')
    list_display_links = ('id', 'full_name')

    def days(self, obj):
        days_diff = (datetime.now() - obj.created_at).days
        if days_diff > 3:
            color = 'red'
        else:
            color = 'purple'
        if obj.solved:
            color = 'green'
        return format_html("<div style='color: {}'>{}</div>", color, days_diff)
