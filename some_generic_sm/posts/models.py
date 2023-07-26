import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Post(models.Model):
    id = models.UUIDField(_('ID'), primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=255)
    content = models.CharField(_('Content'), max_length=255)
    likes = GenericRelation('posts.Like')

    created_at = models.DateTimeField(_('Creation Datetime'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Update Datetime'), auto_now=True)


class Comment(models.Model):
    id = models.UUIDField(_('ID'), primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(_('Content'), max_length=255)
    replying_to = models.ForeignKey('posts.Comment', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    likes = GenericRelation('posts.Like')

    created_at = models.DateTimeField(_('Creation Datetime'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Update Datetime'), auto_now=True)


class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField(_('Content Object ID'))
    content_object = GenericForeignKey('content_type', 'object_id')

    created_at = models.DateTimeField(_('Creation Datetime'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Update Datetime'), auto_now=True)
