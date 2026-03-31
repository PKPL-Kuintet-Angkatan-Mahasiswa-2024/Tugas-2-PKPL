from django.urls import path
from biodata_kelompok.views import *

urlpatterns = [
    path('', show_biodata_homepage)
]
