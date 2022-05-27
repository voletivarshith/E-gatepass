from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test,login_required
from db.models import Gatepass


def is_warden(user):
    if user.is_warden:
        return True
    return False

@login_required
@user_passes_test(is_warden)
def dashboard(request):
    return render(request,"warden/dashboard.html",)

@login_required
@user_passes_test(is_warden)
def print_outing_forms(request):
    return render(request,"warden/view_outing_forms.html",{"forms":Gatepass.objects.filter(is_printed = False,approved=True).order_by("from_date")})

@login_required
@user_passes_test(is_warden)
def approved_outing_forms(request):
    return render(request,"warden/approved_outing_forms.html",{"forms":Gatepass.objects.filter(is_printed = True)})