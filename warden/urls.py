from django.urls import path
from .views import dashboard,print_outing_forms,approved_outing_forms
urlpatterns = [
    path("",dashboard,name="warden-dashboard"),
    path("outing-forms/",print_outing_forms,name="print-outing-forms"),
    path("approved-outing-forms/",approved_outing_forms,name="approved-outing-forms"),
    ]