from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=400,default="Item Description")
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    inventory = models.SmallIntegerField(verbose_name="Inventory Count")
    def __str__(self):
        return self.title