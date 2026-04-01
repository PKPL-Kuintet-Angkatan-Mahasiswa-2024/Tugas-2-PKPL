from django.db import models
from django.conf import settings
from config_models.models import ConfigurationModel


class BiodataTheme(ConfigurationModel):
    PRIMARY_COLOR_CHOICES = [
        ('#6C63FF', 'Purple'),
        ('#0F6E56', 'Teal'),
        ('#D85A30', 'Coral'),
        ('#185FA5', 'Blue'),
    ]

    FONT_CHOICES = [
        ('sans-serif', 'Default'),
        ('Georgia, serif', 'Georgia'),
        ('Verdana, sans-serif', 'Verdana'),
        ('Courier New, monospace', 'Courier New'),
    ]

    primary_color = models.CharField(
        max_length=20,
        choices=PRIMARY_COLOR_CHOICES,
        default='#6C63FF',
        help_text='Warna utama tampilan website'
    )

    font_family = models.CharField(
        max_length=100,
        choices=FONT_CHOICES,
        default='sans-serif',
        help_text='Font yang digunakan di seluruh website'
    )

    class Meta:
        verbose_name = 'Biodata Theme'

    def __str__(self):
        return f"Theme: {self.primary_color} | {self.font_family}"


class Biodata(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"Biodata - {self.user.email}"