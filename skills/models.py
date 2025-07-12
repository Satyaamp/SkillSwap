from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_offered = models.BooleanField(default=True)  # True: offered, False: wanted
    approved = models.BooleanField(default=True)    # Admin moderation (optional)

    def __str__(self):
        return f"{self.name} ({'Offered' if self.is_offered else 'Wanted'}) - {self.user.username}"
