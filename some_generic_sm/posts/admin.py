from some_generic_sm.posts.models import Post
from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at')
    list_filter = ()
    search_fields = ('user', 'title',)
    ordering = ('-id',)


admin.site.register(Post, PostAdmin)
