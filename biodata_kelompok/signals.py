from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from biodata_kelompok.models import Biodata


@receiver(user_signed_up)
def user_signed_up_callback(sender, request, user, **kwargs):
    Biodata.objects.create(user=user, bio="")
