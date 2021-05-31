# Create your models here.

from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
# todo bring back with swag
# from wagtail.admin.edit_handlers import FieldPanel
# from wagtail.core.fields import RichTextField
# from wagtail.core.models import Page
# from wagtail.users.models import UserProfile

from .managers import MyUserManager
# from institutions.models.member_aware_model import MemberAwareModel

USERNAME_REGEX = '^[a-zA-Z0-9.@_]*$'


class MyUser(AbstractBaseUser, PermissionsMixin):  #, MemberAwareModel
    email = models.EmailField(
        db_index=True, verbose_name=_('email address'), max_length=255, unique=True, blank=True, null=True)
    username = models.CharField(
        db_index=True, verbose_name=_('username'), max_length=50, unique=True,
        validators=[RegexValidator(regex=USERNAME_REGEX,
                                   message="Username must be Alpha-Numeric and may also contain '.', '@' and '_'.",
                                   code='Invalid Username.')])
    # institution = ParentalKey('institutions.Institution', db_index=True, to_field='dpid', db_column='dpid',
    #                           on_delete=models.DO_NOTHING, related_name='users', blank=True, null=True)
    # date_of_birth = models.DateField(db_index=True, verbose_name=_('date of birth'), blank=True, null=True)

    first_name = models.CharField(verbose_name=_('first name'), max_length=32, blank=True, null=True)
    last_name = models.CharField(verbose_name=_('last name'), max_length=32, blank=True, null=True)

    is_active = models.BooleanField(default=False, db_index=True, )
    is_admin = models.BooleanField(default=False, db_index=True, )
    is_staff = models.BooleanField(default=False, db_index=True, )

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]  # 'date_of_birth'

    def __str__(self):
        return f"{self.last_name}, {self.first_name} <{self.email}>" if (
                self.last_name and self.first_name
        ) else f"{self.username} <{self.email}>"

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    class Meta:
        # managed = False
        db_table = 'users'
        verbose_name = 'User'
        # unique_together = ('member', 'email')


# todo bring back with swag
# def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         try:
#             UserProfile.objects.create(user=instance)
#         except:
#             pass
# post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)


# class MyUserIndex(Page):
#     intro = RichTextField(blank=True)
#
#     content_panels = Page.content_panels + [
#         FieldPanel('intro', classname="full")
#     ]
