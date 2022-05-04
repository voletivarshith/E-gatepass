from django.contrib.auth.backends import ModelBackend
from .models import User
from django.contrib.admin import ModelAdmin
class EmailBackend(ModelBackend):
    def is_valid_user(self,username=None,password=None):
        try:
            user_obj = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        if user_obj.check_password(password):
            return user_obj
        else:
            return None
        pass
    def authenticate(self, request,username=None,password=None, **kwargs):
        user_obj = self.is_valid_user(username,password)
        if user_obj:
            if request.path=="/admin/login/":
                if user_obj.is_superuser:
                    return user_obj
                else:
                    return None
            else:
                return user_obj
        else:
            return None