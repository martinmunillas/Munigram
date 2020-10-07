from django.urls import path
from munigram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('posts/', posts_views.list_posts)

]
