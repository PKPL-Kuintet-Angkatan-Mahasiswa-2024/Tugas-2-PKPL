from django.contrib import admin
from config_models.admin import ConfigurationModelAdmin
from biodata_kelompok.models import BiodataTheme, Biodata

admin.site.register(BiodataTheme, ConfigurationModelAdmin)
admin.site.register(Biodata)
