from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Pizzeria(models.Model):
    pizzeria_name= models.CharField(max_length=200, blank=False)
    street= models.CharField(max_length=400, blank=True)
    city= models.CharField(max_length=400, blank=True)
    state= models.CharField(max_length=2, null=True, blank=True)
    zip_code= models.IntegerField(blank=True, default=0)
    website = models.URLField(max_length=420, blank=True)
    phone_number = models.CharField(validators=[RegexValidator(regex=r'^\1?\d{9,10}$')], max_length=10, blank=True)
    description = models.TextField(blank=True)
    logo_image = models.ImageField(upload_to='pizzariaImages', blank=True, default="pizzariaImages/pizzalogo.png")
    email = models.EmailField(max_length=245, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}, {}".format(self.pizzeria_name, self.city)