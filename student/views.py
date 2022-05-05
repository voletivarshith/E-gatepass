from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from db.models import User,Department,Gatepass
from .validators import outing_form_validator
from django.contrib import messages

def is_student(request):
    if request.is_student:
        return True
    return False


@login_required
@user_passes_test(is_student)
def dashboard(request):
    return render(request,"student/dashboard.html")


@login_required
@user_passes_test(is_student)
def apply_gatepass(request):
    if request.method=="POST":
        form_is_valid = outing_form_validator(request,request.POST.get("counsellor"),request.POST.get("from_date"),request.POST.get("to_date"))
        if form_is_valid:
            counsellor = User.objects.get(username=request.POST.get("counsellor"))
            print(request.POST.get("Emergency"))
            if request.POST.get("Emergency"):
                emergency=True
            else:
                emergency = False
            Gatepass.objects.create(student=request.user,section=request.POST.get("section"),register_no=request.POST.get("register_no"),year=request.POST.get("year"),counsellor=counsellor,place=request.POST.get("place"),reason_for_leave=request.POST.get("reason_for_leave"),parents_name=request.POST.get("parents_name"),parents_pno=request.POST.get("parents_pno"),is_emergency=emergency,from_date=request.POST.get("from_date"),to_date=request.POST.get("to_date"))
            messages.success(request,"We got your outing form")
            return redirect("student:student-dashboard")
    user_department = Department.objects.get(name=request.user.department)
    return render(request,"student/outing_form.html",{"counsellor":User.objects.filter(department=user_department,is_counsellor=True)})

@login_required
@user_passes_test(is_student)
def previous_outing(request):
    student = User.objects.get(username=request.user)
    context = {"forms":Gatepass.objects.filter(student=student,is_approved=True),"title":"Approved outing forms"}
    return render(request,"student/outing_forms.html",context)

@login_required
@user_passes_test(is_student)
def pending_outing_forms(request):
    student = User.objects.get(username=request.user)
    print(type(request.user))
    context = {"forms":Gatepass.objects.filter(student=student),"title":"Pending outing forms"}
    return render(request,"student/outing_forms.html",context)