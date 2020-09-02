from django.db import models

# Create your models here.


class Meditation(models.Model):
    practice = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    description = models.TextField()
    photo_url = models.TextField()

    def __str__(self):
        return self.practice


class Benefit(models.Model):
    benefit = models.CharField(max_length=100)
    meditation = models.ForeignKey(
        Meditation, on_delete=models.CASCADE, related_name='benefits')

    def __str__(self):
        return self.benefit
