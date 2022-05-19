from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from db.models import Gatepass,User
from django.contrib import messages
from decouple import config
def is_hod(user):
    if user.is_hod:
        return True
    return False

@login_required
@user_passes_test(is_hod)
def dashboard(request):
    return render(request,"hod/dashboard.html")

@login_required
@user_passes_test(is_hod)
def outing_forms(request):
    return render(request,"hod/outing_forms.html",{"forms":Gatepass.objects.filter(year_coordinator_sign=True,approved=False,student__department=request.user.department,deny=False),"title":"Pending outing forms"})


@login_required
@user_passes_test(is_hod)
def denied_outing_forms(request):
    return render(request,"hod/outing_forms.html",{"forms":Gatepass.objects.filter(year_coordinator_sign=True,student__department=request.user.department,deny=True),"title":'Denied outing forms',})

@login_required
@user_passes_test(is_hod)
def approve_outing_form(request,id):
    to_be_approved = Gatepass.objects.get(id=id)
    to_be_approved.hod_sign = True
    to_be_approved.deny = False
    to_be_approved.save()
    messages.error(request,"Approved outing form")
    return redirect("hod:view-outing-forms")

@login_required
@user_passes_test(is_hod)
def deny_outing_form(request,id):
    deny_outing_form = Gatepass.objects.get(id=id)
    deny_outing_form.deny = True
    deny_outing_form.save()
    messages.error(request,"Denied application form")
    return redirect("hod:view-outing-forms")


@login_required
@user_passes_test(is_hod)
def view_students(request):
    return render(request,"hod/view_students.html",{"students":User.objects.filter(department = request.user.department,is_student= True).order_by("year"),"title":"Students"})

@login_required
@user_passes_test(is_hod)
def change_student_password(request,id):
    try:
        student = User.objects.get(id=id)
    except User.DoesNotExist:
        messages.error(request,"Student does not exists")
        return redirect("hod:view_students")
    if student.department!=request.user.department:
        messages.error(request,"You cant access this page")
        return redirect("hod:view-students")
    if request.method=="POST":
        student.set_password(request.POST.get("password"))
        student.save()
        messages.error(request,"Changed user password")
        return redirect("hod:view-students")
    return render(request,"hod/change_password.html")


@login_required
@user_passes_test(is_hod)
def create_student_user(request):
    z = User(username=request.POST.get("username"),email=request.POST.get("email"))
    z.set_password(config("STUDENT_PASSWORD"))
    return render(request,"hod/create_student_user.html",)