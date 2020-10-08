

#Django
from django.contrib import admin

#Models
from posts.models import Post

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'caption', 'photo')
    list_display_links = ('pk', 'user')
    search_fields = (
        'user__email', 
        'user__first_name', 
        'user__last_name', 
        'user__email'
    )

    list_filter = (
        'created', 
        'modified', 
    )

    fieldsets = (
        ('Post', {
            'fields':('user', 'photo', 'caption')
        }),
        ('Meta', {
            'fields': ('created', 'modified',)
        }),

    )
    
    readonly_fields = (
        'created', 'modified', 

    )