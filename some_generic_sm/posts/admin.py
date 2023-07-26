from some_generic_sm.posts.models import Post, Like, Comment
from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at')
    list_filter = ()
    readonly_fields = ('id',)
    search_fields = ('user', 'title',)
    ordering = ('-created_at',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'content', 'created_at')
    list_filter = ()
    readonly_fields = ('id',)
    search_fields = ('user',)
    ordering = ('-created_at',)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content_type', 'object_id', 'created_at')
    list_filter = ()
    readonly_fields = ('id',)
    search_fields = ('user',)
    ordering = ('-created_at',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
