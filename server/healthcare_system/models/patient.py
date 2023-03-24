from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    dob = models.DateField()
    telephone = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    ward_village = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50, default='Test User')
    created = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=50, default='Test User')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'First Name: {self.first_name}, Last Name: {self.last_name}, DOB: {self.dob}'
        
    @property
    def patient_details(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'sex': self.sex,
            'dob': self.dob,
            'telephone': self.telephone,
            'email': self.email,
        }

    class Meta:
        verbose_name_plural = "patients"