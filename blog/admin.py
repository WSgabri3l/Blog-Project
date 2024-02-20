from django.contrib import admin

# Register your models here.

from .models import BlogTitle, BlogText
from .models import PostText, PostTitle

admin.site.register(BlogTitle)
admin.site.register(BlogText)
admin.site.register(PostTitle)
admin.site.register(PostText)