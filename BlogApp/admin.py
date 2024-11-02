from django.contrib import admin
from BlogApp import models
# Register your models here.
admin.site.register(models.Blog)
admin.site.register(models.Comment)
admin.site.register(models.Likes)