from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

ROLES = (
    ('user', 'User'),
    ('moderator', 'Moderator'),
    ('admin', 'Admin')
)


class User(AbstractUser):
    email = models.EmailField(
        blank=False,
        max_length=254,
        unique=True
    )
    bio = models.TextField(max_length=550, null=True, blank=True, verbose_name='О себе')
    role = models.TextField(blank=True, choices=ROLES, default='users')
    username = models.CharField(
        max_length=150,
        verbose_name='Username',
        unique=True,
        null=True,
        validators=[RegexValidator(regex=r'^[\w.@+-]+$', message='Недопустимые символы')]
    )

    @property
    def is_admin(self):
        return self.role == self.is_superuser

    @property
    def is_moderator(self):
        return self.role == "moderator"
