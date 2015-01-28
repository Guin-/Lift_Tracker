from django.contrib import admin
from portal.models import UserProfile

#admin.site.register(User)
admin.site.register(UserProfile)

#class User(admin.ModelAdmin):
#    list_display =('first_name', 'last_name', 'username', 'email')

class UserProfile(admin.ModelAdmin):
    list_display =('user', 'name', 'age' 'bodyweight', 'goals', 'timestamp')
