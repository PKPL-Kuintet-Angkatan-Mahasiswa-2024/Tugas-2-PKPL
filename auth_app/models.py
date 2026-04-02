from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models.functions import Lower


class UserQuerySet(models.QuerySet):
    def authorized(self):
        allowed_emails = [
            e.lower() for e in getattr(settings, "GROUP_MEMBER_EMAILS", [])
        ]
        return (
            self.annotate(email_lower=Lower("email"))
            .filter(
                is_active=True,
                email_lower__in=allowed_emails,
                socialaccount__provider="google",
            )
            .distinct()
        )


class CustomUserManager(UserManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def authorized(self):
        return self.get_queryset().authorized()


class AppUser(AbstractUser):
    objects = CustomUserManager()
