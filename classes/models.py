from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	teacher = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

class Student(models.Model):
	classroom = models.ForeignKey(Classroom, default=1, on_delete=models.CASCADE)
	name = models.CharField(max_length=120)
	date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
	M = 'Male'
	F = 'Female'
	GENDER_CHOICES = ((M, 'Male'), (F, 'Female'))
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='1')
	exam_grade = models.FloatField(default=70)

def __str__(self):
        return self.name