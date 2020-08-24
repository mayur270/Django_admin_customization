from django.db import models

# Create your models here.
class coffee(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='media/' ,blank=True, null=True)

    def __str__(self):
        return self.name

class coffee_file(models.Model):
    csv_file = models.FileField(upload_to='media')
    uploaded = models.DateTimeField(auto_now_add=True, null=True)
    activated = models.BooleanField(default = False)

    def __str__(self):
        return f"File id: {self.id}"
