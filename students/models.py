from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Student(models.Model):
    STUDY_TYPES = (
        ('Редовната форма', 'Редовна форма'),
        ('Задочна форма', 'Задочна форма'),
        ('Дистанционна форма', 'Дистанционна форма'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    faculty_number = models.PositiveIntegerField(null= False, blank= False, unique= True)
    year_of_study = models.PositiveSmallIntegerField(null= False, blank= False,  validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ])
    study_type = models.CharField(max_length=255, null= False, blank= False, choices= STUDY_TYPES)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Course(models.Model):
    EDUCATION_TYPES = (
        ('Бакалавр', 'Бакалавр'),
        ('Магистр', 'Магистр'),
    )
    name = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    education_level = models.CharField(max_length=255, choices=EDUCATION_TYPES)

    def __str__(self):
        return self.name