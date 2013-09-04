from django.contrib import admin
from .models import *

class WebUserAdmin(admin.ModelAdmin):
    pass

class JobAdmin(admin.ModelAdmin):
    pass

admin.site.register(WebsiteUser, WebUserAdmin)
admin.site.register(Job, JobAdmin)