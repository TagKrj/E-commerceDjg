from django.contrib import admin
from userauths.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'bio']
    list_display_links = ['id', 'username']
    search_fields = ['username', 'email']

admin.site.register(User,UserAdmin)
