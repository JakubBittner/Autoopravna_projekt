from django.db import models
from django.contrib.auth.models import User

class Repair(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'Čeká na opravu'),
        ('in_progress', 'Probíhá oprava'),
        ('completed', 'Dokončeno'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Oprava {self.id} - {self.customer.username}"
