from django.db import models

from City.models import City

# Create your models here.


class Admin(models.Model):
  # https://docs.djangoproject.com/en/3.2/ref/models/fields/
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=250, unique=True, null=True)
  password = models.CharField(max_length=200)
  is_main = models.BooleanField(default=False)
  image = models.ImageField(upload_to='admin/images')
  city = models.ManyToManyField(City, blank=True, null=True)

  def __str__(self):
    return f'{self.name} - {self.is_main}'

  def underscored_name(self):
    return self.name.replace(' ','_')


class Phone(models.Model):
  phone = models.CharField(max_length=20)
  lindline = models.CharField(max_length=20)
  admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.phone}'