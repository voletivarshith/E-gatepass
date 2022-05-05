from django.urls import path,include
from superuser.views import createsuperuser
from db.views import user_login,user_logout
from django.contrib import admin
from student.views import dashboard
urlpatterns = [
    path('secret-path/', include(("superuser.urls","superuser"),namespace="superuser")),
    path("principal/",include(("principal.urls","principal"),namespace="principal")),
    path("student/",include(("student.urls","student"),namespace="student")),
    path("",user_login,name="login"),
    path("google/",admin.site.urls,name="super-user"),
    path("logout/",user_logout,name="logout")
]