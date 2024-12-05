from django.db import models
import uuid

# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    price = models.CharField(max_length=5,  null=False, blank=False)
    location = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable= False)

    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
