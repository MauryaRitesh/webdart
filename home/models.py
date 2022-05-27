from django.db import models
#from home.models import Contact

#makemigrations - create changes  and store in a file
#migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model): 
   name = models.CharField(max_length=120)
   email = models.CharField(max_length=30)
   address = models.CharField(max_length=20)
   number = models.CharField(max_length=12)
   city = models.CharField(max_length=20)
   state = models.CharField(max_length=20)
   code = models.CharField(max_length=6)

class Profile(models.Model):
   name = models.CharField(max_length = 30, default = '')
   def __str__(self):
      return self.name
    