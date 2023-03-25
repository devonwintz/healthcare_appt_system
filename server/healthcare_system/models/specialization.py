from django.db import models

class Specialization(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.CharField(max_length=50, default='Test User')
    created = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=50, default='Test User')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Name: {self.name}'
    
    @property
    def specialization_details(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    class Meta:
        verbose_name_plural = "specializations"