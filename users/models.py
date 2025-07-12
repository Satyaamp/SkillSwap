from django.db import models
from django.contrib.auth.models import User

AVAILABILITY_CHOICES = [
    ('weekends', 'Weekends'),
    ('evenings', 'Evenings'),
    ('both', 'Weekends and Evenings'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, blank=True)
    is_public = models.BooleanField(default=True)
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
