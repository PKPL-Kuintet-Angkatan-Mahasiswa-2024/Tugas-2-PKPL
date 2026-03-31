from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from biodata_kelompok.models import Biodata
from biodata_kelompok.forms import BiodataForm
from django.contrib import messages
from allauth.socialaccount.models import SocialAccount

def is_authorized(user):
    if not user.is_authenticated:
        return False

    email = (user.email or "").lower()
    allowed_emails = [e.lower() for e in getattr(settings, 'GROUP_MEMBER_EMAILS', [])]
    is_group_member = email in allowed_emails

    has_google_login = SocialAccount.objects.filter(
        user=user,
        provider="google"
    ).exists()

    return is_group_member and has_google_login


def show_biodata_homepage(request):
    context = {
        'biodata_list': Biodata.objects.all(),
        'is_authorized': is_authorized(request.user),
    }
    return render(request, "biodata.html", context)


@login_required
def edit_biodata(request):
    if not is_authorized(request.user):
        messages.error(request, "You are not authorized to edit biodata.")
        return redirect('biodata:homepage')

    biodata, _ = Biodata.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = BiodataForm(request.POST, instance=biodata)
        if form.is_valid():
            form.save()
            return redirect('biodata:homepage')
    else:
        form = BiodataForm(instance=biodata)

    return render(request, "edit_biodata.html", {'form': form})