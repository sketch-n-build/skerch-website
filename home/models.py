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
    imagelink = models.CharField(max_length=1000,default='https://res.cloudinary.com/skaetch/image/upload/v1602166969/skaetch/assets/img/blog/single_blog_4_jsrgae.png')
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 375 or img.width > 750:
    #         output_size = (750, 375)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
class EventWeeks(models.Model):
    week_number = models.CharField(max_length=10)
    event_id = models.CharField(default='nav-week-WeekNumber-tab', max_length=100)
    href = models.CharField(default='#nav-week-Weeknumber', max_length=100)
    aria_controls = models.CharField(default='nav-week-WeekNumber', max_length=100)

    def __str__(self):
        return self.week_number

    class Meta:
        verbose_name_plural = "Event Weeks"

class EventDetails(models.Model):
    event_week = models.OneToOneField(EventWeeks,on_delete=models.CASCADE)
    event_heading = models.CharField(default='Skaetch And Build', max_length=100)
    activity = models.CharField(default='Skaetch And Build', max_length=1000) 
    activity_time = models.DateField(default=timezone.now())  
    detail_point1 = models.CharField(default='Skaetch And Build', max_length=1000)
    detail_point2 = models.CharField(default='Skaetch And Build', max_length=1000)
    detail_point3 = models.CharField(default='Skaetch And Build', max_length=1000)

    def __str__(self):
        return self.event_heading

    class Meta:
        verbose_name_plural = "Event Details"