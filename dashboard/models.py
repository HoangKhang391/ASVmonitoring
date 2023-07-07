from django.db import models
from django.contrib.auth.hashers import make_password
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Response_From_Web(models.Model):
    zone = models.IntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"Zone {self.zone}: ({self.latitude}, {self.longitude})"


class Data_From_ASV(models.Model):
    humidity = models.FloatField()  # Correct the field name
    temperature = models.FloatField()
    dissolvedOxygen = models.FloatField()
    airPressure = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data_From_ASV {self.id}: {self.humidity}, {self.temperature}, {self.dissolvedOxygen}, {self.airPressure}, {self.latitude}, {self.longitude}"
