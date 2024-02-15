#from django.db import models

# Create your models here.
from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_contact = models.BooleanField(default=False)
    is_opportunity = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Opportunity(models.Model):
    opportunities = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    close_date = models.DateField()
    stage = models.CharField(max_length=100)
    probability = models.IntegerField()
    type = models.CharField(max_length=100)
    lead_source = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    lead = models.ForeignKey('Lead', on_delete=models.CASCADE)


    def __str__(self):
        return self.opportunities
