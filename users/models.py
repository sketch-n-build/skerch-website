from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    age = models.IntegerField(blank=True, null=True)
    country = models.CharField(blank=True, max_length=100)
    state = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=100)
    address = models.CharField(blank=True, max_length=200)
    phone = models.CharField(blank=True, max_length=100)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} profile pics'


    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)