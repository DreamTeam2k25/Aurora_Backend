from django.contrib import admin

from core.uploader.models import Image, Document

# Register your models here.
admin.site.register(Image)
admin.site.register(Document)