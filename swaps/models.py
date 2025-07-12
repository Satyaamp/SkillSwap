from django.db import models
from django.contrib.auth.models import User
from skills.models import Skill
from users.models import UserProfile

SWAP_STATUS = [
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
    ('cancelled', 'Cancelled')
]

class SwapRequest(models.Model):
    sender = models.ForeignKey(User, related_name='sent_swaps', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_swaps', on_delete=models.CASCADE)
    offered_skill = models.ForeignKey(Skill, related_name='offered_swaps', on_delete=models.CASCADE)
    requested_skill = models.ForeignKey(Skill, related_name='requested_swaps', on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=SWAP_STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} → {self.receiver.username} [{self.status}]"

class Feedback(models.Model):
    swap = models.OneToOneField(SwapRequest, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return f"Feedback on swap #{self.swap.id}"

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
