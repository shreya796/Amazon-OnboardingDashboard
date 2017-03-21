from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    #locker_id = models.IntegerField(primary_key=True,default=1,auto_created=True)
    locker_name = models.CharField(max_length=200)
    city = models.TextField()
    state = models.TextField()
    Pincode = models.TextField()
    capacity = models.IntegerField(default=100)
    ratio = models.FloatField()