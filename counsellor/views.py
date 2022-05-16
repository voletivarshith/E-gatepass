from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from db.models import Gatepass
from django.contrib import messages

def is_counsellor(user):
    if user.is_counsellor:
        return True
    return False


@login_required
@user_passes_test(is_counsellor)
def dashboard(request):
    return render(request,"counsellor/dashboard.html")

@login_required
@user_passes_test(is_counsellor)
def view_outing_forms(request):
    return render(request,"counsellor/view_outing_forms.html",{"forms":Gatepass.objects.filter(counsellor=request.user,approved=False,is_emergency=False,deny=False,counsellor_sign=False)})

@login_required
@user_passes_test(is_counsellor)
def approve_outing_form(request,id):
    to_be_approved = Gatepass.objects.get(id=id)
    to_be_approved.counsellor_sign = True
    to_be_approved.deny=False
    to_be_approved.save()
    messages.success(request,"Outing form forwarded to the Year coordinator")
    return redirect("counsellor:view-outing-forms")

@login_required
@user_passes_test(is_counsellor)
def deny_outing_form(request,id):
    deny_form = Gatepass.objects.get(id=id)
    deny_form.deny=True
    deny_form.save()
    messages.success(request,"Outing form denied")
    return redirect("counsellor:view-outing-forms")

@login_required
@user_passes_test(is_counsellor)
def denied_outing_forms(request):
    return render(request,"counsellor/denied_outing_forms.html",{"forms":Gatepass.objects.filter(counsellor=request.user,approved=False,is_emergency=False,deny=True)})