from django.urls import path
from .views import dashboard,view_outing_forms,denied_outing_forms,approve_outing_form,deny_outing_form

urlpatterns = [
    path("",dashboard,name="year-coordinator-dashboard"),
    path("view-outing-forms/",view_outing_forms,name="view-outing-forms"),
    path("denied-outing-forms/",denied_outing_forms,name="denied-outing-forms"),
    path("approve-outing-form/<int:id>/",approve_outing_form,name="approve-outing-form"),
    path("deny-outing-form/<int:id>/",deny_outing_form,name="deny-outing-form")
]