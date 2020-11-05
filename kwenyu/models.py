from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Neighbourhood (models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    picture = CloudinaryField('image')
    admin = models.ForeignKey(User, on_delete=models.CASCADE,related_name='admin')    

    def __str__(self):
        return self.name

    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    profile_photo = CloudinaryField('image')
    status=models.CharField(max_length=50,blank=True)
    neighbourhood = models.ForeignKey('Neighbourhood', on_delete=models.CASCADE, blank=True,default= 1)

    def __str__(self):
        return self.name

class Business(models.Model):
    business_pic = CloudinaryField('image')
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return self.name

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()


