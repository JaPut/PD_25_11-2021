from django.contrib import admin

from .models import User

class VisitUser(admin.ModelAdmin):
    pass

admin.site.register(User, VisitUser)