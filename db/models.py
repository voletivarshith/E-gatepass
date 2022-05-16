from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.forms
class Department(models.Model):
    name = models.CharField(max_length=101)
    def __str__(self):
        return self.name


class User(AbstractUser):
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            "Check this if the user is super user(Super user has the highest privilages)"
        ),
    )
    is_staff = models.BooleanField(
        _('Principal status'),
        default=False,
        help_text=_('If principal Check this'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'To block the user uncheck this'
        ),
    )
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(_("Student"),default=True,help_text=_("If student check this"))
    is_year_coordinator = models.BooleanField(_("Year Coordinator"),default=False,help_text=_("If year coordinator check this"))
    is_counsellor = models.BooleanField(_("Counsellor"),default = False,help_text=_("If Counsellor check this"))
    is_hod = models.BooleanField(_("HOD"),default=False,help_text=_("If HOD check this"))
    is_warden = models.BooleanField(_("Warden"),default=False,help_text=_("If warden check this"))
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    year = models.IntegerField(null=True)
    def save(self,*args,**kwargs):
        if(self.is_year_coordinator or self.is_counsellor or self.is_staff or self.is_superuser or self.is_hod or self.is_warden):
            self.is_student = False
        super().save(*args,**kwargs)
    def __str__(self):
        return self.username


class Gatepass(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name="student")
    section = models.CharField(max_length=2)
    register_no = models.CharField(max_length=15)
    year = models.IntegerField()
    counsellor = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="Counsellor")
    year_coordinator = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,name="Year coordinator")
    applied_date = models.DateField()
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    place = models.CharField(max_length=101)
    reason_for_leave = models.TextField(max_length=1001)
    parents_name = models.CharField(max_length=101)
    parents_pno = models.CharField(max_length=15)
    parents_permission = models.BooleanField(default=False)
    is_emergency = models.BooleanField(default=False)
    counsellor_sign = models.BooleanField(default=False)
    year_coordinator_sign = models.BooleanField(default=False)
    hod_sign = models.BooleanField(default=False)
    principal_sign = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    deny = models.BooleanField(default=False)
    def save(self,*args,**kwargs):
        if self._state.adding:
            from datetime import date
            self.applied_date = date.today()
        if(self.hod_sign or self.principal_sign):
            self.approved = True
        if self.deny:
            self.counsellor_sign = False
            self.year_coordinator_sign = False
            self.principal_sign = False
        super().save(*args,**kwargs)
    def __str__(self):
        return str(self.student)+"**Outing**"+str(self.applied_date)