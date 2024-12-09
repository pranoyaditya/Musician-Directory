from django.db import models
from Musician_app.models import Musician

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    album_release_date = models.DateField()

    RATING_CHOICES = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]

    ratings = models.IntegerField(choices=RATING_CHOICES) # Stores the rating as an integer
    Musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.album_name} by {self.Musician.first_name}'

