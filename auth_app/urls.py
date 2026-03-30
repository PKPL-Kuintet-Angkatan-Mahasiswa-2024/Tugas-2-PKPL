from django.urls import path
from auth_app.views import *

urlpatterns = [
    path('logout', home)
]
