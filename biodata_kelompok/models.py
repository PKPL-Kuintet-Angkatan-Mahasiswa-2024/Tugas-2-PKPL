from django.db import models
from authentication_and_authorization import settings
from config_models.models import ConfigurationModel


class BiodataTheme(ConfigurationModel):
    pass


class Biodata(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
