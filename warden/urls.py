from django.urls import path
from .views import dashboard,print_outing_forms,approved_outing_forms,print_outing_form
urlpatterns = [
    path("",dashboard,name="warden-dashboard"),
    path("outing-forms/",print_outing_forms,name="print-outing-forms"),
    path("approved-outing-forms/",approved_outing_forms,name="approved-outing-forms"),
    path("print-outing-form/<int:id>/",print_outing_form,name="print-outing-form")
    ]