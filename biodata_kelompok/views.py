from django.http import HttpRequest
from django.shortcuts import render
from biodata_kelompok.models import Biodata


def show_biodata_homepage(request: HttpRequest):
    return render(request, "biodata.html", {'biodata_list': Biodata.objects.all()})

