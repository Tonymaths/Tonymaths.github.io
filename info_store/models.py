from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=130)
    email=models.CharField(max_length=130)
    number=models.DecimalField(max_digits=12, decimal_places=0)
    contact=models.CharField(max_length=130)


    def __str__(self):
         return self.name


#pythonmanage.py migrate --run-syncd if migration fails
