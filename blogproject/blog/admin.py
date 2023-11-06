from django.contrib import admin

from .models import Post
# from blog.models import Post


class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'status', 'created_on', 'updated_on', ]
  list_filter = ('status', 'created_on',)
  search_fields = ('body', 'title',)
  prepopulated_fields = {
    'slug': ('title',)
  }

# Register your models here.
admin.site.register(Post, PostAdmin)
