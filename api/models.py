from django.db import models

# Create your models here.
class Talaba(models.Model):
    first_name = models.CharField(max_length = 124)
    last_name = models.CharField(max_length = 124)
    age = models.IntegerField()
    country = models.CharField(max_length = 124)

    def __str__(self):
        return self.first_name
    
