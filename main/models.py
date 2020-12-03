from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_post", kwargs={"pk": self.pk})
