from django.contrib import admin
from posts.models import Category, Post

# Register your models here.
# admin.site.register(User)
admin.site.register(Post)
admin.site.register(Category)

