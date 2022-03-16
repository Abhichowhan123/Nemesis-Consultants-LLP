from django.db import models

# Create your models here.
class customer (models.Model):
    Name= models.CharField(max_length= 50)
    Username = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=13)
    Password = models.CharField(max_length=100)
    Address = models.CharField(max_length=250)


    def get_customer_by_email(Email):
        try:
            return customer.objects.get(email = Email)
        except:
            return False

    def __str__(self):
        return self.Name