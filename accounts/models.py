#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class AccountUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True, verbose_name="用户名")
    first_name = models.CharField(max_length=100, blank=True, verbose_name="名")
    last_name = models.CharField(max_length=100, blank=True, verbose_name="姓")
    email = models.EmailField(max_length=100, unique=True, verbose_name="邮箱地址")
    # nickname = models.CharField(max_length=20, blank=True, verbose_name="昵称")
    phone = models.CharField(max_length=20, blank=True, verbose_name="手机号码")
    # head_avatar = models.ImageField(upload_to='./avatars', default="./avatars/default.png", blank=True, verbose_name="头像")
    # head_oauth_avatar = models.URLField(blank=True, verbose_name="oauth头像")
    # description = models.TextField(blank=True, verbose_name="描述")
    sex = models.CharField(max_length=10, blank=True, verbose_name="性别")
    # birthday = models.DateTimeField(auto_now_add=True, verbose_name="生日")
    is_active = models.BooleanField(default=True, verbose_name="激活")
    # activate_key = models.SlugField(max_length=40, blank=True)
    is_staff = models.BooleanField(default=False, verbose_name="管理员")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="加入时间")

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    class Meta:
        ordering = ('-date_joined',)
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # @property
    # def is_staff(self):
    #     return self.is_superuser
