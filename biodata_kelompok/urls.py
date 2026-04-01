from django.urls import path

from biodata_kelompok.views import edit_biodata, edit_tampilan, show_biodata_homepage

app_name = "biodata"

urlpatterns = [
    path("", show_biodata_homepage, name="homepage"),
    path("edit-biodata/", edit_biodata, name="edit_biodata"),
    path("edit-tampilan/", edit_tampilan, name="edit_tampilan"),
]
