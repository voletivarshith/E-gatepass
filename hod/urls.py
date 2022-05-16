from django.urls import path
from .views import dashboard,approve_outing
urlpatterns = [
    path("",dashboard,name="hod-dashboard"),
    path("approve-outing/",approve_outing,name="approve-outing")
]