from django.db import models
from .doctor import Doctor
from .patient import Patient

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=50, default='incomplete')
    created_by = models.CharField(max_length=50, default='Test User')
    created = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=50, default='Test User')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Date: {self.date}, Start Time: {self.start_time}, End Time: {self.end_time}'

    
    class Meta:
        verbose_name_plural = "appointments"
