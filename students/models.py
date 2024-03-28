from django.db import models

# Create your models here.
class Students(models.Model):
    code = models.CharField(max_length=6,unique=True)
    name = models.TextField()

    def __str__(self):
        return self.name
    