from allauth.socialaccount.models import SocialAccount
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from biodata_kelompok.forms import BiodataForm, BiodataThemeForm
from biodata_kelompok.models import Biodata, BiodataTheme

ANGGOTA_LIST = [
    {"nama": "Karla Ameera Raswanda", "npm": "2406414542"},
    {"nama": "Raida Khoyyara", "npm": "2406495445"},
    {"nama": "Josh Christmas Rommlynn", "npm": "2406395291"},
    {"nama": "Muhammad Fadhlurrohman Pasya", "npm": "2406411830"},
    {"nama": "Christopher Evan Tanuwidjaja", "npm": "2406358056"},
]


def is_authorized(user):
    if not user.is_authenticated:
        return False

    email = (user.email or "").lower()
    allowed_emails = [e.lower() for e in getattr(settings, "GROUP_MEMBER_EMAILS", [])]
    is_group_member = email in allowed_emails

    has_google_login = SocialAccount.objects.filter(
        user=user, provider="google"
    ).exists()

    return is_group_member and has_google_login


def get_active_theme():
    """Ambil tema aktif dari database (ConfigurationModel)."""
    try:
        return BiodataTheme.current()
    except Exception:
        return None


def show_biodata_homepage(request):
    theme = get_active_theme()

    context = {
        "anggota_list": Biodata.objects.all(),
        "is_authorized": is_authorized(request.user),
        "theme": theme,
    }
    return render(request, "biodata.html", context)


@login_required
def edit_biodata(request):
    if not is_authorized(request.user):
        messages.error(request, "You are not authorized to edit biodata.")
        return redirect("biodata:homepage")

    biodata, _ = Biodata.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = BiodataForm(request.POST, instance=biodata)
        if form.is_valid():
            form.save()
            return redirect("biodata:homepage")
    else:
        form = BiodataForm(instance=biodata)

    return render(request, "edit_biodata.html", {"biodata": biodata})


@login_required
def edit_tampilan(request):
    if not is_authorized(request.user):
        messages.error(request, "Kamu tidak memiliki akses untuk mengubah tampilan.")
        return redirect("biodata:homepage")

    theme = get_active_theme()

    if request.method == "POST":
        form = BiodataThemeForm(request.POST, instance=theme)
        if form.is_valid():
            form.save()
            return redirect("biodata:homepage")

    context = {
        "theme": theme,
        "color_choices": [
            ("#6C63FF", "Purple"),
            ("#0F6E56", "Teal"),
            ("#D85A30", "Coral"),
            ("#185FA5", "Blue"),
        ],
        "font_choices": [
            ("sans-serif", "Default"),
            ("Georgia, serif", "Georgia"),
            ("Verdana, sans-serif", "Verdana"),
            ("Courier New, monospace", "Courier New"),
        ],
    }
    return render(request, "edit_tampilan.html", context)
