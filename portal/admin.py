from django.contrib import admin
from portal.models import UserProfile

admin.site.register(UserProfile)


class UserProfile(admin.ModelAdmin):
    list_display =('user', 'name', 'age' 'bodyweight', 'goals', 'timestamp')
