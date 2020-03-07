from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions  import ValidationError

# Create your models here.


def validate_file_size(value):
    if value.size>7340032:
        raise ValidationError('File size cannot be more than 7MB')
    else:
        return value
def default_user():
    return User.objects.get(pk=1).pk
class Result(models.Model):
    choices = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]

    filename = models.CharField(max_length=100,unique=True,blank=False,default='NoFile')
    prediction = models.CharField(max_length=70,unique=False,blank=False,choices=choices)
    date=  models.DateTimeField(blank=False,auto_now_add=True)
    user = models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)





class File(models.Model):
    filepath = models.ImageField(upload_to='uploads/')
    uploaded_user = models.ForeignKey(User,related_name='uploaded_user',on_delete=models.PROTECT)
    

    def __str__(self):
        return str(self.filepath)   
     
class Bill(models.Model):
    user = models.ForeignKey(User,related_name='user_bill',on_delete=models.PROTECT)
    date= models.DateTimeField(blank=False,auto_now_add=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2,blank=False)     