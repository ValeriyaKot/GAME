from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birthday = models.DateField(validators=[MaxValueValidator(datetime.now().date())], blank=True, null=True)

    def __str__(self):
        return self.user.username
