from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.



class admin_registration(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4, editable = False)
    name_of_org = models.CharField(max_length=30, unique=True)
    year_of_foundation = models.IntegerField()
    contact_number = models.IntegerField()
    username = models.CharField(max_length= 10, unique= True)
    email = models.EmailField(unique= True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s is Admin " % self.name_of_org


class user_registration(models.Model):

    Male = 'M'
    Female = 'F'
    Transgender = 'TRANS'

    gender_choices = [
        (Male, 'Male'),
        (Female, 'Female'),
        (Transgender, 'Transgender'),
    ]
    name_of_org = models.ForeignKey(admin_registration, on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=30, unique= True)
    gender = models.CharField(max_length=12, choices= gender_choices, default= Male)
    username = models.CharField(max_length= 10, unique= True)
    email = models.EmailField(unique= True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return "%s is User " % self.name