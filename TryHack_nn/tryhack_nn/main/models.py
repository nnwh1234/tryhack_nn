from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    content = models.TextField()
    mood = models.CharField(
        max_length=20,
        choices = [
            ('Happy', 'Happy'),
            ('Upset', 'Upset'),
            ('Anxious', 'Anxious'),
            ('Sad', 'Sad'),
            ('Neutral', 'Neutral')
        ]
    )

    def __str__(self):
        return self.title