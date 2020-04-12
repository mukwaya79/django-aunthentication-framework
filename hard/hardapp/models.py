from django.db import models

# Create your models here.


class Register(models.Model): 

    Firstname = models.CharField(max_length=50, null=False)
    Lastname = models.CharField(max_length=50, null=False)
    Password = models.CharField(max_length=20, null=False, unique=True)
    Email = models.EmailField(max_length=50 ,unique=True)
    Mobile = models.IntegerField()
    Address= models.TextField(max_length=100,null=False)
    Gender = models.CharField(max_length=20)
    Hobbies = models.CharField(max_length=20,null=False)
    Date = models.DateField(null=False)
    Country = models.CharField(max_length=50,null=False)
    File = models.ImageField()

    def __str__(self):
       return "%s %s" %(self.Firstname,self.Lastname)
