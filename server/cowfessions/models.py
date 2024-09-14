from django.db import models
from user.models import User

# Create your models here.

class Cowfession(models.Model):

    cowfession_text = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.cowfession_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)