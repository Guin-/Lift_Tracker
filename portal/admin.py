from django.contrib import admin
from portal.models import User


admin.site.register(User)

class User(admin.ModelAdmin):
    list_display =('first_name', 'last_name', 'username', 'email')

