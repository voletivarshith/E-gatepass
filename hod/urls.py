from django.urls import path
from .views import dashboard,outing_forms,denied_outing_forms,deny_outing_form,approve_outing_form,view_students,change_student_password
urlpatterns = [
    path("",dashboard,name="hod-dashboard"),
    #URL's for outing forms
    path("outing-forms/",outing_forms,name="view-outing-forms"),
    path("approve-outing-forms/<int:id>/",approve_outing_form,name="approve-outing-form"),
    path("deny-outing-form/<int:id>/",deny_outing_form,name="deny-outing-form"),
    path("denied-outing-forms/",denied_outing_forms,name="denied-outing-forms"),
    #URL's for modifying student
    path("view-students/",view_students,name="view-students"),
    path("change-password/<int:id>/",change_student_password,name="change-student_password")
]