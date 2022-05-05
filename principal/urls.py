from django.urls import path
from .views import dashboard, view_approved_outing_forms,view_outing_forms,approve_outing_form,deny_outing_forms,denied_outing_forms
urlpatterns = [
    path("",dashboard,name="principal-dashboard"),
    path("outing-forms/",view_outing_forms,name="outing-forms"),
    path("approved-outing-forms/",view_approved_outing_forms,name="previous-outing-forms"),
    path("denied-outing-forms",denied_outing_forms,name="denied-outing-forms"),
    path("approve-outing-form/<int:id>/",approve_outing_form,name="approve-outing-form"),
    path("deny-outing-forms/<int:id>/",deny_outing_forms,name="deny-outing-form")
    ]