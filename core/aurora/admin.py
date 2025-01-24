from django.contrib import admin

from core.aurora.models import PostImage, Posts

admin.site.register(Posts)
admin.site.register(PostImage)