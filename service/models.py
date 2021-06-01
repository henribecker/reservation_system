from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name