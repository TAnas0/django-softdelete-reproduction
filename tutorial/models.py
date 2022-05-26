from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)

class Employee(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
