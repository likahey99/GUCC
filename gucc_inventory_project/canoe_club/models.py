from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.template.defaultfilters import slugify


# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField("is admin", default=False)
    is_member = models.BooleanField("is member", default=True)
    email = models.EmailField(unique=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    picture = models.ImageField(upload_to="profile_images", blank=True)


class Trip(models.Model):
    NAME_MAX_LENGTH = 255
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    location = models.CharField(max_length=128)
    date = models.DateField()
    length = models.IntegerField(default=0)
    members = models.ManyToManyField(UserProfile)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Trip, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Kit(models.Model):
    NAME_MAX_LENGTH = 40
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True, primary_key=True)
    size = models.IntegerField()
    colour = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)  # link to member id
    type = models.CharField(max_length=20)
    maintenance_problem = models.CharField(null=True, blank=True, max_length=20)
    maintenance = models.BooleanField(default=True)
    amount = models.IntegerField(default=0)
    image = models.ImageField(upload_to='kit_images', blank=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Kit, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Social(models.Model):
    NAME_MAX_LENGTH = 255
    DETAILS_MAX_LENGTH = 255
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    date = models.DateField()
    details = models.CharField(max_length=DETAILS_MAX_LENGTH)
    location = models.CharField(max_length=128)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Social, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
