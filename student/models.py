from django.db import models

# Create your models here.
class Student(models.Model):
    number=models.PositiveIntegerField()
    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    email=models.EmailField()
    note=models.DecimalField(max_digits=4,decimal_places=2)
    photo=models.ImageField(upload_to='student_photos/%y/%m/%d',null=True,blank=True)
    def __str__(self):
        return f'Student :{self.first_name} {self.last_name}'
    
         