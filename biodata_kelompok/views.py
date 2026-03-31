from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from biodata_kelompok.models import Biodata
from biodata_kelompok.forms import BiodataForm


def show_biodata_homepage(request):
    return render(request, "biodata.html", {'biodata_list': Biodata.objects.all()})


@login_required
def edit_biodata(request):
    if request.method == 'POST':
        form = BiodataForm(request.POST, instance=request.user.biodata)
        if form.is_valid():
            form.save()
            return redirect('biodata:homepage')
    return render(request, "edit_biodata.html", {'form': BiodataForm(instance=request.user.biodata)})
