from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager
from django.db import models
from django.contrib.auth.models import Group,Permission
class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_admin', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, password, **extra_fields)

class VrUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=240, unique=True) 
    first_name = models.CharField(max_length=240, blank=True, null=True)
    last_name = models.CharField(max_length=240, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    mobile_number = models.CharField(max_length=240, unique=True, blank=True, null=True)
    is_Vruser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name', 'mobile_number']

    class Meta:
        verbose_name = 'VrUsers'

    def __str__(self):
        return self.email

class VrUserGroup(models.Model):
    user = models.ForeignKey(VrUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class VrUserPermission(models.Model):
    user = models.ForeignKey(VrUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)