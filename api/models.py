from django.db import models

# Create your models here.
class Worker(models.Model):
    
    name  = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    value   = models.IntegerField(default=0)
    def __str__(self):
        return self.name


class Farmer(models.Model):
    name = models.CharField(max_length=50,blank=False)
    phone = models.IntegerField(max_length=11,blank=False)
    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=50,blank=False)
    phone = models.IntegerField(max_length=11,blank=False)
    def __str__(self):
        return self.name

class Farm(models.Model):
    name = models.CharField(max_length=30,blank=False)
    farmer = models.ForeignKey(Farmer,blank=False)
    def __str__(self):
        return self.name +":"+ self.farmer


class Daily_Harvest_Result(models.Model):
    date = models.DateField(auto_now_add=True,blank=False)
    farm_id = models.ForeignKey(Farm,blank=False)
    farmer_id = models.ForeignKey(Farmer,blank=True)
    worker_id = models.ForeignKey(Worker,blank=False)
    value = models.FloatField(default=0)
    def __str__(self):
        return str(id)
