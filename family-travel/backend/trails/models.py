from django.db import models
from django.contrib.auth.models import User

class Trail(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Легкая'),
        ('medium', 'Средняя'),
        ('hard', 'Сложная'),
    ]
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    description = models.TextField()
    keywords = models.CharField(max_length=300)
    duration = models.CharField(max_length=50)
    accommodation = models.CharField(max_length=200, blank=True, null=True)
    coordinates = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TrailImage(models.Model):
    trail = models.ForeignKey(Trail, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='trail_photos/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

class IncludedService(models.Model):
    trail = models.ForeignKey(Trail, related_name='included_services', on_delete=models.CASCADE)
    service = models.CharField(max_length=100)

class AvailableDate(models.Model):
    trail = models.ForeignKey(Trail, related_name='available_dates', on_delete=models.CASCADE)
    date = models.DateField()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trail = models.ForeignKey(Trail, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trail = models.ForeignKey(Trail, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'trail')

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    date = models.DateField()
    people_count = models.PositiveIntegerField()
    full_name = models.CharField(max_length=150)
    passport_data = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
