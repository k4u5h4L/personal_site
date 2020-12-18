from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    what_i_do = models.CharField(max_length=500)

    def __str__(self):
        return self.title