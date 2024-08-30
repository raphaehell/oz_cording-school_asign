from django.contrib import admin

from blog.models import Blog

@admin.register(Blog)
class ModelNameAdmin(admin.ModelAdmin):
    ...

