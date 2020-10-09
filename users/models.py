from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    full_name = models.CharField(blank=True, max_length=300)
    age = models.IntegerField(blank=True, null=True)
    country = models.CharField(blank=True, max_length=100)
    state = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=100)
    address = models.CharField(blank=True, max_length=200)
    phone = models.CharField(blank=True, max_length=100)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_volunteer = models.BooleanField(default=False)
    level = models.IntegerField(blank=True,default=1)
    group = models.CharField(blank=True, max_length=100)
    points = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return f'{self.user.username}'


    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Achievements(models.Model):
    achievement_name = models.CharField(blank=True, max_length=300)
    color_code = models.CharField(default='#00000', blank=True, max_length=100)
    user = models.ManyToManyField(User)
    date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.achievement_name

    class Meta:
        verbose_name_plural = "Achievements"