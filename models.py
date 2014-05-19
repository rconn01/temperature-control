from django.db import models

class Sensor(models.Model):
    sensorName = models.CharField(max_length=200)
    sensorLocation = models.CharField(max_length=200)
    sensorBrand= models.CharField(max_length=200,blank=True)
    sensorIntroductionDate = models.DateTimeField()
    sensorMeta = models.CharField(max_length=250,blank=True)	

class Reading(models.Model):
    sensor=models.ForeignKey(Sensor)
    value = models.DecimalField(max_digits=7,decimal_places=4)
    date = models.DateTimeField('date of reading')
    lastModifedDate = models.DateTimeField(auto_now="true")   
    

class DayReading(models.Model):
    sensor = models.ForeignKey(Sensor)
    date = models.DateField()
    high = models.DecimalField(max_digits=7,decimal_places=4)
    low = models.DecimalField(max_digits=7,decimal_places=4)
    median = models.DecimalField(max_digits=7,decimal_places=4)
    average= models.DecimalField(max_digits=7,decimal_places=4)
    notesForDay= models.TextField()
