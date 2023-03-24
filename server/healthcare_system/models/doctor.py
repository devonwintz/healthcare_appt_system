from django.db import models
from .specialization import Specialization

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialization = models.ManyToManyField(Specialization)
    telephone = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    created = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50, default='Test User')
    created = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=50, default='Test User')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"First Name: {self.first_name}, Last Name: {self.last_name}, Specialization: {self.specialization.values_list('name', flat=True)}"
    
    @property
    def doctor_details(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'specialization': self.specialization.values_list('name', flat=True),
            'email': self.email,
            'telephone': self.telephone,
        }

    class Meta:
        verbose_name_plural = "doctors"