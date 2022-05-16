from django.urls import path
from .views import dashboard,view_outing_forms,approve_outing_form,deny_outing_form,denied_outing_forms
urlpatterns = [
    path("",dashboard,name="counsellor-dashboard"),
    path("view-outing-forms/",view_outing_forms,name="view-outing-forms"),
    path("approve-outing-forms/<int:id>/",approve_outing_form,name="approve-outing-form"),
    path("deny-outing-forms/<int:id>/",deny_outing_form,name="deny-outing-form"),
    path("denied-outing-forms/",denied_outing_forms,name="denied-outing-forms")
]