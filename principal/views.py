from django.shortcuts import render,redirect
from db.models import Gatepass
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib import messages

def principal_view(user):
    if user.is_staff:
        return True
    else:
        return False

@login_required
@user_passes_test(principal_view)
def dashboard(request):
    return render(request,"principal/dashboard.html")

@login_required
@user_passes_test(principal_view)
def view_outing_forms(request):
    return render(request,"principal/outing_forms.html",{"forms":Gatepass.objects.filter(is_emergency=True,approved=False,deny=False)})

@login_required
@user_passes_test(principal_view)
def view_approved_outing_forms(request):
    return render(request,"principal/previous_forms.html",{"forms":Gatepass.objects.filter(principal_sign=True)})

@login_required
@user_passes_test(principal_view)
def approve_outing_form(request,id):
    to_be_approved = Gatepass.objects.get(id=id)
    to_be_approved.principal_sign=True
    to_be_approved.deny=False
    to_be_approved.save()
    messages.success(request,"Approved for outing")
    return redirect("principal:outing-forms")

@login_required
@user_passes_test(principal_view)
def deny_outing_forms(request,id):
    to_deny_outing_forms = Gatepass.objects.get(id=id)
    to_deny_outing_forms.deny = True
    to_deny_outing_forms.save()
    messages.success(request,"Denied for outing")
    return redirect("principal:outing-forms")

@login_required
@user_passes_test(principal_view)
def denied_outing_forms(request):
    return render(request,"principal/denied_outing_forms.html",{"forms":Gatepass.objects.filter(deny=True,is_emergency=True)})