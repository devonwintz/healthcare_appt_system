"""healthcare_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from healthcare_system import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', views.PatientView.patient_list),
    path('patients/<int:id>', views.PatientView.patient_details),
    path('doctors/', views.DoctorView.doctor_list),
    path('doctors/<int:id>', views.DoctorView.doctor_details),
    path('specializations/', views.SpecializationView.specialization_list),
    path('specializations/<int:id>', views.SpecializationView.specialization_details),
    path('emergency-contacts/', views.EmergencyContactView.emergency_contact_list),
    path('emergency-contacts/<int:id>', views.EmergencyContactView.emergency_contact_details),
    path('allergies/', views.AllergyView.allergy_list),
    path('allergies/<int:id>', views.AllergyView.allergy_details),
    path('appointments/', views.AppointmentView.appointment_list),
    path('appointments/<int:id>', views.AppointmentView.appointment_details),
    path('auth-token/', obtain_auth_token),
]


urlpatterns = format_suffix_patterns(urlpatterns)
