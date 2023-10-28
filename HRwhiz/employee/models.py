from django.db import models
# Create your models here.

class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=80)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=30)
    address=models.CharField(max_length=255)
    designation=models.CharField(max_length=80, default='Manager')
    sick_leave=models.IntegerField(default=12)
    casual_leave=models.IntegerField(default=5)
    annual_leave=models.IntegerField(default=5)
    phone_number=models.IntegerField()
    pid=models.ForeignKey('Project',on_delete=models.CASCADE)
    did=models.ForeignKey('Department',on_delete=models.CASCADE)
    manager_id=models.ForeignKey('Employee',on_delete=models.CASCADE,null=True,blank=True)
    status=models.BooleanField(default=False)
    profile_url=models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name_plural='Employee'

class Department(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    leader_id=models.ForeignKey('Employee',on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        verbose_name_plural='Department'

class Project(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    leader_id=models.ForeignKey('Employee',on_delete=models.CASCADE,null=True,blank=True)
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
    fed_by=models.ForeignKey('Employee',on_delete=models.CASCADE,related_name='given_feedback', null=True, blank=True)
    fed_to=models.ForeignKey('Employee',on_delete=models.CASCADE,related_name='recieved_feedback', null=True, blank=True)
    type=models.CharField(max_length=50)
    fed_body=models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural='Feedbacks'
    

    

