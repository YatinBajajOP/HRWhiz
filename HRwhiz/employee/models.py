from django.db import models
# Create your models here.

class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=80)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    sick_leave=models.IntegerField()
    casual_leave=models.IntegerField()
    annual_leave=models.IntegerField()
    phone_number=models.IntegerField()
    pid=models.ForeignKey('Project',on_delete=models.CASCADE)
    did=models.ForeignKey('Department',on_delete=models.CASCADE)
    manager_id=models.ForeignKey('Employee',on_delete=models.CASCADE,null=True)
    status=models.BooleanField()
    profile_url=models.CharField(max_length=30)

    class Meta:
        verbose_name_plural='Employee'

class Department(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    # leader_id=models.IntegerField()

    class Meta:
        verbose_name_plural='Department'

class Project(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    # leader_id=models.ForeignKey('Employee',on_delete=models.CASCADE)
    did=models.ForeignKey('Department',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Project'

class Requests(models.Model):
    id=models.IntegerField(primary_key=True)
    req_by=models.ForeignKey('Employee',on_delete=models.CASCADE,related_name='request_made')
    req_to=models.ForeignKey('Employee',on_delete=models.CASCADE,related_name='request_recieved')
    type=models.CharField(max_length=50)
    req_body=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural='Requests'

class Feedback(models.Model):
    id=models.IntegerField(primary_key=True)
    fed_by=models.ForeignKey('Employee',on_delete=models.CASCADE,related_name='given_feedback')
    fed_to=models.ForeignKey('Employee',on_delete=models.CASCADE,related_name='recieved_feedback')
    type=models.CharField(max_length=50)
    fed_body=models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural='Feedback'
    

    

