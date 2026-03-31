from django.urls import path
from biodata_kelompok.views import *

app_name = 'biodata'
urlpatterns = [
    path('', show_biodata_homepage, name='homepage'),
    path('edit_biodata/', edit_biodata, name='edit_biodata'),
]
