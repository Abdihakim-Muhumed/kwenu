from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = CloudinaryField('image')
    neighbourhood = models.ForeignKey('Neighbourhood', on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return self.name

class Neighbourhood (models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    picture = CloudinaryField('image')
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE)    
    health = models.IntegerField(null=True, blank=True)
    police = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()