from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200 , unique= True)
    phone_number = models.BigIntegerField()
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    
    def __str__(self) -> str:
        return self.name