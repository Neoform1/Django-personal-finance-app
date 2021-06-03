from django.contrib import admin

# Register your models here.
from .models import Profile
from .models import Transaction

# registering our models for admin site
admin.site.register(Profile)
admin.site.register(Transaction)

