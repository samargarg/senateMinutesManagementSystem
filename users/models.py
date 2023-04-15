#
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#
#
# class OperatorManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError("Email is Required!")
#         user = self.model(email=self.normalize_email(email))
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password=None):
#         if not email:
#             raise ValueError("Email is Required!")
#         user = self.model(email=self.normalize_email(email))
#         user.set_password(password)
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
#
#
# class Operator(AbstractBaseUser):
#     email = models.EmailField(max_length=60, unique=True)
#     username = models.CharField(max_length=30, null=True, blank=True, default="_")
#     dateJoined = models.DateTimeField(auto_now_add=True)
#     lastLogin = models.DateTimeField(auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#
#     objects = OperatorManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     def __str__(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         return self.is_admin
#
#     def has_module_perms(self, app_label):
#         return True
#
