from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Ticket(models.Model):
    CHOICES = (
        ('Oczekuje', 'Oczekuje'),
        ('W trakcie', 'W trakcie'),
        ('Naprawiono', 'Naprawiono'),
        ('Odrzucone', 'Odrzucone')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=CHOICES, default=CHOICES[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Device(models.Model):
    name = models.CharField(max_length=1000)
    purchase_date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
