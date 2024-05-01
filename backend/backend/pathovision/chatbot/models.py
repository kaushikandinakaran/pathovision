from django.db import models

# Create your models here.

class question_master(models.Model):
    qust_id = models.AutoField(primary_key=True)
    qust_title = models.CharField(max_length=100, unique=True)
    is_enabled = models.IntegerField(max_length=1, default=1)

class question_details(models.Model):
    qust_d_id = models.AutoField(primary_key=True)
    qust_id = models.IntegerField()
    questions = models.CharField(max_length=500, unique=True)
    qust_type = models.IntegerField(default=1)
    order = models.IntegerField(default=1)
    parent_id = models.IntegerField(default=0)
    is_enabled = models.IntegerField(max_length=1, default=1)

class option_details(models.Model):
    option_id = models.AutoField(primary_key=True)
    qust_d_id = models.IntegerField()
    option = models.CharField(max_length=100, unique=True)
    order = models.IntegerField(default=1)
    is_enabled = models.IntegerField(max_length=1, default=1)

class schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    doctor_id = models.IntegerField()
    patient_id = models.IntegerField()
    date = models.dateField()
    time_from = models.timeField()
    time_to = models.timeField()
