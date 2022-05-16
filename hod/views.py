from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from db.models import Gatepass
def is_hod(user):
    if user.is_hod:
        return True
    return False

@login_required
@user_passes_test(is_hod)
def dashboard(request):
    pass

@login_required
@user_passes_test(is_hod)
def approve_outing(request):
    return render(request,"hod/approve_outing.html",{"forms":Gatepass.objects.filter(year_coordinator_sign=True)})