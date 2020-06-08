from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
class Repo(models.Model):
    name = models.CharField(primary_key = True, max_length = 200)
    stars = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    html_url = models.CharField(max_length=200)

    def create(a,b, c, d):
        name = a
        stars = b
        created_date = c
        html_url = d

    def __str__(self):
        return self.name
