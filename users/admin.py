

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

#Models
from users.models import Profile

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'user', 'website', 'picture')
#     list_display_links = ('pk', 'user')
#     list_editable = ('website', 'picture')
#     search_fields = (
#         'user__email', 
#         'user__first_name', 
#         'user__last_name', 
#         'user__email'
#     )

#     list_filter = (
#         'created', 
#         'modified', 
#         'user__is_staff'
#     )

#     fieldsets = (
#         ('Profile', {
#             'fields':('user', 'picture')
#         }),
#         ('Extra', {
#             'fields':(('website', 'phone_number'), ('biography',))
#         }),
#         ('Meta', {
#             'fields': ('created', 'modified',)
#         }),

#     )
    
#     readonly_fields = (
#         'created', 'modified', 'user'

#     )

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'last_name',
        'is_active',
        'is_staff',
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)