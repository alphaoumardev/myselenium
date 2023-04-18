# Register your models here.
from django.contrib import admin

from .models import Category, InstagramAccount, InstagramPost, InstagramAccountReport, \
    Hashtag

# Register your models here.

admin.site.register(Category)
admin.site.register(InstagramAccount)
admin.site.register(InstagramPost)
admin.site.register(InstagramAccountReport)
admin.site.register(Hashtag)
