from django.urls import path
from .views import dashboard,apply_gatepass, pending_outing_forms,previous_outing,view_outing_forms
urlpatterns = [
    path("",dashboard,name="student-dashboard"),
    path("apply-gatepass/",apply_gatepass,name="apply-gatepass"),
    path("previous-outing-forms/",previous_outing,name="previous-outing"),
    path("view-outing-forms/",pending_outing_forms,name="view-outing-forms"),
]