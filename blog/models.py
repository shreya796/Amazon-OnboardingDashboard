from django.db import models


#from __future__ import unicode_literals


class Table1(models.Model):
    locker_id = models.IntegerField(primary_key=True)
    locker_name = models.CharField(db_column='Locker_name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    pincode = models.CharField(max_length=45, blank=True, null=True)
    prime_capacity = models.CharField(max_length=45, blank=True, null=True)
    standard_capacity = models.CharField(max_length=45, blank=True, null=True)

"""
    class Meta:
        managed = False
        db_table = 'table1'
        """
        
