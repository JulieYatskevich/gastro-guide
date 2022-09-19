from django.contrib.auth.models import User
from django.db import models
from .choices import category_choices, kitchen_choices, rating_choices
from datetime import datetime


class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200)
    photo = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=20, choices=category_choices, default='cafe', blank=True, null=True)
    kitchen = models.CharField(max_length=20, choices=kitchen_choices, default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="restaurant")
    rating = models.IntegerField(choices=rating_choices, null=False)
    date_visited = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f'{self.reviewer.username} : {self.restaurant.name}'
