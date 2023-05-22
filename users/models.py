from django.db import models
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, user_name, first_name, password, **other_fields):
        
        if not email:
            raise ValueError(_("Users must have an email address"))
        
        user = self.model(email=self.normalize_email(email), user_name=user_name,
                          first_name=first_name, **other_fields)
        
        user.set_password(password) # create password field and hash it
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must be assigned is_staff to True'))

        if other_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must be assigned is_superuser to True'))
        return self.create_user(email, user_name, first_name, password, **other_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    # image = models.ImageField(default='')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self) -> str:
        return self.user_name
    
    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()
    