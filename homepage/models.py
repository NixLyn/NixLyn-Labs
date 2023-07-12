from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    add_on = models.TextField(max_length=255, default="ADD_FUNDS")
    date_made  = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.title) + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse('homepage')



