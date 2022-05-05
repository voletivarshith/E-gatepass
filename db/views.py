from django.shortcuts import render,redirect
from django.urls import reverse
from db.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def user_login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            z = User.objects.get(username=user)
            login(request,user)
            if request.user.is_superuser:
                print("redirecting")
                return redirect("superuser:super-user-dashboard")
            elif request.user.is_staff:
                return redirect("principal:principal-dashboard")
            elif request.user.is_hod:
                return redirect("hod:")
            elif request.user.is_year_coordinator:
                pass
            elif request.user.is_counsellor:
                pass
            elif request.user.is_student:
                return redirect("student:student-dashboard")
        else:
            messages.error(request,"Invalid username or password")
    return render(request,"db/login.html",)


def user_logout(request):
    logout(request)
    return redirect("login")
