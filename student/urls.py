from django.urls import path
from .views import dashboard,apply_gatepass,previous_outing
urlpatterns = [
    path("",dashboard,name="student-dashboard"),
    path("apply-gatepass/",apply_gatepass,name="apply-gatepass"),
    path("previous-outing-forms",previous_outing,name="previous-outing")
    ]