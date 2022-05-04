from django.shortcuts import render
from db.models import Gatepass
from django.contrib.auth.decorators import user_passes_test

def principal_view(user):
    if user.is_principal:
        return True
    else:
        return False

@user_passes_test(principal_view)
def view_outing(request):
    return render(request,"principal/outing.html",{"forms":Gatepass.objects.filter(is_emergency=True,approved=False)})