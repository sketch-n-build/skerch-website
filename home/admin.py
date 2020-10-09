from django.contrib import admin
from .models import Post,ContactUs,EventWeeks,EventDetails

admin.site.register(Post)
admin.site.register(ContactUs)
admin.site.register(EventWeeks)
admin.site.register(EventDetails)