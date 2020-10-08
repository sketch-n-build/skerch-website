from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100 , blank=True)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Us"

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default='This is the default text, for more click the title')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='blog_pics')

    def __str__(self):
        return self.title


    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 375 or img.width > 750:
            output_size = (750, 375)
            img.thumbnail(output_size)
            img.save(self.image.path)
