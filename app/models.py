from django.db import models
from travel_memories.users.models import User

# Create your models here.
class Location(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
  lat = models.DecimalField(max_digits=10, decimal_places=7)
  lng = models.DecimalField(max_digits=10, decimal_places=7)
  title = models.CharField(max_length=255)
  note = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-created_at']
    verbose_name = 'Location'
    verbose_name_plural = 'Locations'
  