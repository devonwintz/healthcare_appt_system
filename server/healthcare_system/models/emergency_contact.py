from django.db import models
from .patient import Patient

class Emergency_Contact(models.Model):
    patient = models.ManyToManyField(Patient)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    telephone = models.CharField(max_length=10)
    email = models.EmailField(blank=True)
    created = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50, default='Test User')
    created = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=50, default='Test User')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'First Name: {self.first_name}, Last Name: {self.last_name}, Relationship: {self.relationship}'

    class Meta:
        verbose_name_plural = "emergency contacts"
