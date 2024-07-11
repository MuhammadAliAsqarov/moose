from django.urls import path
from .views import home_view, blog_view, about_view, contact_view, blog_detail_view

urlpatterns = [
    path('', home_view),
    path('moose/blog/', blog_view),
    path('moose/about/', about_view),
    path('moose/contact/', contact_view),
    path('moose/blog/<int:pk>/', blog_detail_view),
]
