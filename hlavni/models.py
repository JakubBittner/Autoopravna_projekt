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
        return self.title

class RepairReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rezervace {self.user.username} na {self.date} {self.time}"
