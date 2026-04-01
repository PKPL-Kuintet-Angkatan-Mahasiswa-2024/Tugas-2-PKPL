from django.urls import path
from biodata_kelompok.views import show_biodata_homepage, edit_tampilan

app_name = 'biodata'

urlpatterns = [
    path('', show_biodata_homepage, name='homepage'),
    path('edit-tampilan/', edit_tampilan, name='edit_tampilan'),
]