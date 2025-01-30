from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    



class MOU(models.Model):
    Id = models.AutoField(primary_key=True)  # Use AutoField for auto-incrementing primary key
    Partner = models.CharField(max_length=255)
    Sector = models.CharField(max_length=255)
    Purpose = models.CharField(max_length=255)
    Department = models.CharField(max_length=255)
    Duration = models.CharField(max_length=255)

    class Meta:
        db_table = 'MOU'

class CreateMOU(models.Model):
    sector = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    first_party = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    second_party = models.CharField(max_length=255)
    preamble = models.TextField()
    purpose = models.TextField()
    pdf_doc = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.first_party
