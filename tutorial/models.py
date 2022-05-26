from django.db import models
from softdelete.models import SoftDeleteObject

class Company(SoftDeleteObject, models.Model):
    name = models.CharField(max_length=255)

class Employee(SoftDeleteObject, models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
