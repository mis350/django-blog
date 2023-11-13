from django.contrib import admin

from .models import Post, Comment
# from blog.models import Post


class CommentInline(admin.TabularInline):
  model = Comment


class CommentAdmin(admin.ModelAdmin):
  pass

class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'status', 'created_on', 'updated_on', ]
  list_filter = ('status', 'created_on',)
  search_fields = ('body', 'title',)
  prepopulated_fields = {
    'slug': ('title',)
  }
  inlines = [CommentInline,]

# Register your models here.
admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, CommentAdmin)
