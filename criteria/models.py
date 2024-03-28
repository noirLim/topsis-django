from django.db import models
from students.models import Students

# Create your models here.
class Criteria(models.Model):
    code = models.CharField(max_length=6,unique=True)
    name = models.TextField()
    attribute = models.CharField(max_length=20)
    weight = models.FloatField()

    def __str__(self):
        return f'{self.name}'


class Alternative(models.Model):
    student= models.ForeignKey(Students,on_delete=models.CASCADE)
    criteria = models.ForeignKey(Criteria,on_delete=models.CASCADE)
    value = models.FloatField()
