from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test
from db.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def createuser(request):
    if request.method=="POST":
        permission = request.POST.get("permission",[])
        print(request.POST.get("permission"))
        try:
            username = request.POST.get("username")
            User.objects.get(username=username)
            messages.error(request,"Username already exists")
        except User.DoesNotExist:
            flag=1
            try:
                email = request.POST.get("email")
                User.objects.get(email=email)
                messages.error(request,"Email already exists")
            except User.DoesNotExist:
                user_obj = User(username=username,email=email)
                if permission =='Student':
                    user_obj.is_student=True
                elif permission == "Counsellor":
                    user_obj.is_counsellor=True
                elif permission == "Yearcoordinator":
                    user_obj.is_year_coordinator=True
                elif permission == "HOD":
                    user_obj.is_hod=True
                elif permission == "Principal":
                    user_obj.is_staff=True
                else:
                    messages.error(request,"Select a permission")
                    flag=0
                if flag:
                    user_obj.set_password(request.POST.get("password"))
                    user_obj.save()
                    messages.success(request,"Successfully created account")
    return render(request,"superuser/createuser.html")


def createsuperuser(request):
    if request.method=="POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        try:
            User.objects.get(username=username)
            messages.error(request,"Username already exists")
        except User.DoesNotExist:
            try:
                User.objects.get(email=email)
                messages.error(request,"Email already exists")
            except User.DoesNotExist:
                user_obj = User.objects.create_user(username=username,email=email,password=request.POST.get("password"))
                messages.success(request,"Successfully created superuser")
                user_obj.is_superuser=True
                user_obj.save()
    return render(request,"superuser/createsuperuser.html")


@login_required
@user_passes_test(is_superuser)
def dashboard(request):
    return render(request,"superuser/dashboard.html")


@login_required
@user_passes_test(is_superuser)
def users(request,num=1):
    if num==1:
        active_users_query = User.objects.filter(is_staff=True,is_active=True)
        #Principal
    elif num==2:
        active_users_query = User.objects.filter(is_hod=True,is_active=True)        #HOD
    elif num==3:
        active_users_query = User.objects.filter(is_year_coordinator=True,is_active=True)
        #year coordinator
    elif num==4:
        active_users_query = User.objects.filter(is_counsellor=True,is_active=True)
        #counsellor
    elif num==5:
        active_users_query = User.objects.filter(is_student=True,is_active=True)
        #Student
    else:
        messages.error(request,"Invalid url")
    return render(request,"superuser/users.html",{"active_users_query":active_users_query})

@login_required
@user_passes_test(is_superuser)
def delete_user(request,num):
    try:
        user_obj = User.objects.get(id=num)
        messages.success(request,"Successfully deleted user")
        user_obj.is_active = False
        user_obj.save()
    except User.DoesNotExist:
        messages.error(request,"User does not exists")
    return redirect("superuser:super-user-dashboard")

@login_required
@user_passes_test
def user_details(request,num):
    pass