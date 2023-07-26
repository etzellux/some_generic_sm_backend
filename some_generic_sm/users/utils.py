from django.db import models


def get_user_events(user):
    return user.post_set.all().prefetch_related(
        'likes',
        'comments'
    ).order_by(
        '-created_at'
    ).annotate(
        content_type=models.Value('post')
    ).values(
        'id',
        'content_type',
        'created_at'
    ).union(
        user.like_set.filter(
            comment=None
        ).prefetch_related(
            'post'
        ).annotate(
            content_type=models.Value('like_post')
        ).values(
            'post__id',
            'content_type',
            'created_at',
        )
    ).union(
        user.comment_set.all().annotate(
            content_type=models.Value('comment')
        ).values(
            'id',
            'content_type',
            'created_at'
        )
    ).order_by(
        '-created_at'
    )
