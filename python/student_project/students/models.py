from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    math_marks = models.IntegerField()
    science_marks = models.IntegerField()
    physics_marks = models.IntegerField()

    def __str__(self):
        return self.name
