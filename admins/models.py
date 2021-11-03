from django.db import models

# Create your models here.


class Admin(models.Model):
  # https://docs.djangoproject.com/en/3.2/ref/models/fields/
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=250, unique=True, null=True)
  password = models.CharField(max_length=200)
  is_main = models.BooleanField(default=False)
  image = models.ImageField(upload_to='admin/images')

  def __str__(self):
    return f'{self.name} - {self.is_main}'

  def underscored_name(self):
    return self.name.replace(' ','_')