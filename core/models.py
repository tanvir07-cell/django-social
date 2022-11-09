from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(
        upload_to='profile-images', default='blank_profile.png')

    location = models.CharField(max_length=100, blank=True)

    # how to i see the user's list in the admin panel:

    def __str__(self):
        return self.user.username
