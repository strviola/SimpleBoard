from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
class PosterManager(BaseUserManager):
    def create_user(self, username, screen_name, email, password):
        if not username:
            # username must be satisfied
            raise ValueError
        
        user = self.model(username=username,
                          screen_name=screen_name,
                          email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_super_user(self, username, screen_name, email, password):
        user = self.create_user(username, screen_name, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Poster(AbstractBaseUser):
    username = models.CharField(verbose_name='User name', db_index=True,
                                max_length=32, unique=True)
    screen_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=256)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['screen_name', 'email']
    
    def __unicode__(self):
        return '%s (%s) email: %s' % (self.screen_name, self.username,
                                      self.email)
