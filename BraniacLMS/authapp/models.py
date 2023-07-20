from django.db import models
from pathlib import Path
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.mail import send_mail
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _
from time import time

def users_avatars_path(instance, filename):
    num = int(time() * 1000)
    suff = Path(filename).suffix
    file_name=f"pic_{num}{suff}"
    return f"user_{instance.username}/avatars/{file_name}"


class MyUser(AbstractBaseUser, PermissionsMixin):
    username_validator = ASCIIUsernameValidator()

    username = models.CharField(
        _("username"), 
        max_length=150, 
        unique=True, 
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_only." ),
        validators=[username_validator], 
        error_messages={"unique": _("A user with that username already exists."),},
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. \
            Unselect this instead of deleting accounts."
        ),
    )

    email=models.EmailField(
        unique=True, 
        error_messages={"unique": _("A user with that username already exists.")})
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    name = models.CharField(_("first name"), max_length=150, blank=True)
    surname = models.CharField(_("last name"), max_length=150, blank=True)
    age = models.PositiveIntegerField(
        blank=True, null=True,validators=[MaxValueValidator(limit_value=100)]
        )
    avatar = models.ImageField(
        upload_to=users_avatars_path, blank=True, null=True
    )

    objects = UserManager()
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
    
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_short_name(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

