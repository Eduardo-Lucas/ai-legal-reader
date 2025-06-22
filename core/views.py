from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

def home_view(request):
    message = _("Welcome to our site.")
    return render(request, "core/home.html")
