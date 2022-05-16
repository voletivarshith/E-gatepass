from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from db.models import Gatepass
from django.contrib import messages

def logged_user_year_coordinator(user):
    if user.is_year_coordinator:
        return True
    return False

@login_required
@user_passes_test(logged_user_year_coordinator)
def dashboard(request):
    return render(request,"year_coordinator/dashboard.html")

@login_required
@user_passes_test(logged_user_year_coordinator)
def view_outing_forms(request):
    return render(request,"year_coordinator/view_outing_forms.html",{"forms":Gatepass.objects.filter(approved=False,counsellor_sign = True,student__year=request.user.year),"title":"Pending outing forms"})

@login_required
@user_passes_test(logged_user_year_coordinator)
def denied_outing_forms(request):
    return render(request,"year_coordinator/view_outing_forms.html",{"forms":Gatepass.objects.filter(approved=False,counsellor_sign = True,student__year = request.user.year,deny=False),"title":'Denied outing forms'})

@login_required
@user_passes_test(logged_user_year_coordinator)
def approve_outing_form(request,id):
    to_be_approved = Gatepass.objects.get(id=id)
    to_be_approved.year_coordinator_sign = True
    to_be_approved.deny = False
    to_be_approved.save()
    messages.error(request,"Forwaded application to the HOD")
    return redirect("year_coordinator:view-outing-forms")

@login_required
@user_passes_test(logged_user_year_coordinator)
def deny_outing_form(request,id):
    deny_outing_form = Gatepass.objects.get(id=id)
    deny_outing_form.deny = True
    deny_outing_form.save()
    messages.error(request,"Denied application form")
    return redirect("year_coordinator:view-outing-forms")

