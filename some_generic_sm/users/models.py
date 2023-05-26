import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import RegexValidator
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name=_('Email'), unique=True, db_index=True)
    username = models.CharField(_('Username'), max_length=150, unique=True, validators=[RegexValidator(settings.USERNAME_REGEX, _('Username is invalid. Only lowercase English letters, period and underscore characters are allowed. Minimum length is three characters.'))])
    first_name = models.CharField(_('First Name'), max_length=255)
    last_name = models.CharField(_('Last Name'), max_length=255, blank=True)
    is_active = models.BooleanField(verbose_name=_('Active Status'), default=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    profile_picture = models.ImageField(_('Profile Picture'), upload_to='profile_pictures/%Y/%m/%d %H:%M', max_length=255, null=True, blank=True)
    bio = models.TextField(_('Bio'), max_length=255, blank=True)
    signup_date = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ('first_name', 'last_name')

        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email_constaint'),
        ]

        indexes = [
            models.Index(fields=['username'])
        ]