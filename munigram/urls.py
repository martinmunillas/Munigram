from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from munigram import views as local_views

urlpatterns = [

    path('admin/', admin.site.urls, name='admin'),

    path('', include(('posts.urls', 'posts'), namespace='posts')),

    path('users/', include(('users.urls', 'users'), namespace='users')),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
