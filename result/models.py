from django.db import models
from students.models import Students

# Create your moels here.
class Result (models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    date = models.DateField()

class Det_Result(models.Model):
    student = models.ForeignKey(Students,on_delete=models.CASCADE)
    result = models.ForeignKey(Result,on_delete=models.CASCADE)
    value = models.FloatField()
    