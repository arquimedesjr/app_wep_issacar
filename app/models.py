import datetime

from django import forms
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Tribo(models.Model):
    # MY_CHOICES = (
    #     ('Rúben', 'Rúben'),
    #     ('Simeão', 'Simeão'),
    #     ('Levi', 'Levi'),
    #     ('Judá', 'Judá'),
    #     ('Issacar', 'Issacar'),
    #     ('Zebulun', 'Zebulun'),
    #     ('Benjamim', 'Benjamim'),
    #     ('Naftali', 'Naftali'),
    #     ('Gade', 'Gade'),
    #     ('Aser', 'Aser'),
    #     ('Manassés', 'Manassés'),
    #     ('Efraim', 'Efraim'),
    # )
    nome_tribo = models.CharField(max_length=250, null=False)

    class Meta:
        verbose_name_plural = "Tribo"

    def __str__(self):
        return self.nome_tribo


class Grupo(models.Model):
    # MY_CHOICES_GRUPO = (
    #     ('Imbatível', 'Imbatível'),
    #     ('Invencível', 'Invencível'),
    # )
    nome_grupo = models.CharField(max_length=250, null=False)

    class Meta:
        verbose_name_plural = "Grupo"

    def __str__(self):
        return self.nome_grupo


class Jovens(models.Model):
    foto = models.ImageField(upload_to='profile_pics', verbose_name='Foto')
    nome = models.CharField(max_length=250, null=False, verbose_name='Nome - Ex: (Arquimedes Junior)')
    telefone = models.CharField(max_length=11, null=False, verbose_name='Telefone - Ex: 11948924982')
    tribo = models.ForeignKey(Tribo, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    MY_CHOICES = (
        ('SIM', 'SIM'),
        ('NÃO', 'NÃO'),
    )
    presenca = models.CharField(max_length=3, choices=MY_CHOICES, verbose_name='Está na Reunião?', default='NÃO')
    data = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Jovens"

    def __str__(self):
        return self.nome


class Reuniao(models.Model):
    reuniao = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Reunião"

    def __str__(self):
        return self.reuniao


class Relatorio(models.Model):
    qnt = models.IntegerField()
    tribo = models.ForeignKey(Tribo, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Relatorio"

    def __str__(self):
        return str(self.data)

#
# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError("Email invalido")
#
#         if not username:
#             raise ValueError("Usuario invalido")
#
#         user = self.model(
#             username=username,
#             email=self.normalize_email(email),
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password,
#             username=username,
#         )
#
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
#
#
# # Create your models here.
# class Account(AbstractBaseUser):
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     # first_name = models.CharField(max_length=30)
#     # tribo = models.ForeignKey(Tribo, default=1, on_delete=models.CASCADE)
#     # grupo = models.ForeignKey(Grupo, default=1, on_delete=models.CASCADE)
#     date_joined = models.DateTimeField(verbose_name="data joined", auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
#
#     objects = MyAccountManager()
#
#     def __str__(self):
#         return self.username
#
#     def has_perm(self, perm, obj=None):
#         return self.is_admin
#
#     def has_module_perms(self, app_label):
#         return True
#
#     def _get_all_groups(self):
#         if self.is_anonymous() or not self.is_authenticated():
#             return set()
#         if not hasattr(self, '_group_cache'):
#             self._group_cache = set("%s" % (g.name) for g in self.groups.all())
#         return self._group_cache
#
#     def has_group(self, group_perm):
#         if not self.is_active:
#             return False
#         return group_perm in self._get_all_groups()
#
#     def has_groups(self, groups_list):
#         if not self.is_active:
#             return False
#         return groups_list in self._get_all_groups()
