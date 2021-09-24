from django.db import models

# Create your models here.
class student_data(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(max_length=100)
    grade = models.FloatField(max_length=100)
    result = models.CharField(max_length=100)
