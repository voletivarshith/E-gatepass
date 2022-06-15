from django.contrib import admin
from .models import User,Department,Gatepass
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    #is_staff = Principal
    #is_superuser = Super user
    list_display=("username","email")
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_student','is_counsellor',  'is_year_coordinator', 'is_hod', 'is_staff', 'is_superuser',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_("Deparment"),{'fields': ('department','year')})
    )
class GatepassAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields.get("student").queryset = User.objects.filter(is_student=True)
        form.base_fields.get("counsellor").queryset = User.objects.filter(is_counsellor=True)
        form.base_fields.get("Year coordinator").queryset = User.objects.filter(is_year_coordinator=True)
        return form
admin.site.register(User,CustomUserAdmin)
admin.site.register(Department)
admin.site.register(Gatepass,GatepassAdmin)