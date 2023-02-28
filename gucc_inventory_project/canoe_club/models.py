from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    ADMIN = 1
    MEMBER = 2
    ROLE_CHOICES = ((ADMIN, 'Admin'),
                    (MEMBER, 'Memeber'))

    base_role = ADMIN
    user_type = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)

    def get_absolute_url(self):
        return reverse("users:detail",kwargs= {"username":self.username})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = self.base_role
            return super().save(*args, **kwargs)

class MemberManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(user_type = User.MEMBER)

class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(user_type = User.ADMIN)

class Member(User):
    base_role = User.MEMBER
    member = MemberManager()
    class Meta:
        proxy = True

class Admin(User):
    base_role = User.ADMIN
    admin = AdminManager()
    class Meta:
        proxy = True

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_images", blank=True)

class Page(models.Model):
    title = models.CharField(max_length=128)
    url = models.URLField()
    picture = models.ImageField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Trip(models.Model):
    name = models.CharField(max_length=128, unique=True)
    location = models.CharField(max_length=128)
    date = models.DateField()
    length = models.IntegerField(default=0)
    member = models.CharField(max_length=8)

    def __str__(self):
        return self.name


