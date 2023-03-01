from django.db import models
from .patient import Patient 

class Allergy(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    symptom = models.CharField(max_length=255)
    medication = models.CharField(max_length=255, blank=True)
    created_by = models.CharField(max_length=50, default='Test User')
    created = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=50, default='Test User')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Name: {self.name}, Symptoms: {self.symptom}'

    class Meta:
        verbose_name_plural = "allergies"