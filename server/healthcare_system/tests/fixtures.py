from faker import Faker
import random
from ..models import *

fake = Faker()


def patient():
    fullname = fake.name()
    sex = random.sample(["M", "F"], 1)
    village_ward = random.sample(["Kitty", "Sophia"], 1)

    return Patient.objects.create(
        first_name=fullname.split()[0],
        last_name=fullname.split()[1],
        sex=sex,
        dob=fake.date(),
        telephone="5926000000",
        email=f"{fullname.split()[0].lower()+fullname.split()[1].lower()}@example.com",
        address_line_1=fake.street_address(),
        ward_village=village_ward,
        city=fake.city(),
        country=fake.country()
    )

def doctor():
    fullname = fake.name()
    spc = random.sample(list(enumerate(["Allergy and immunology", "Anesthesiology", "Dermatology", "Neurology"])), random.randrange(1,4))

    doctor = Doctor.objects.create(
        first_name=fullname.split()[0],
        last_name=fullname.split()[1],
        telephone="5926000000",
        email=f"{fullname.split()[0].lower()+fullname.split()[1].lower()}@example.com"
    )
    doctor.specialization.set([random.randrange(1,4)])
    return doctor

def appointment():
    doc = doctor()
    doc.save()
    pat = patient()
    pat.save()

    return Appointment.objects.create(
        doctor=doc,
        patient=pat,
        date="2022-09-30",
        start_time="12:30:00",
        end_time="13:30:00",
        status="incomplete"
    )

def allergy():
    pat = patient()
    pat.save()

    symp = []
    med = []

    for i in range(5):
        symp.append(fake.text(max_nb_chars=15))
        med.append(fake.text(max_nb_chars=15))

    return Allergy.objects.create(
        patient=pat,
        name=fake.text(max_nb_chars=15),
        symptom=symp,
        medication=med
    )


def emergency_contact():
    pat = patient()
    pat.save()

    fullname = fake.name()
    relation = random.sample(["Wife", "Husband", "Sibling", "Mother"," Father", "Cousin", "Friend"], 1)

    contact = Emergency_Contact.objects.create(
        first_name=fullname.split()[0],
        last_name=fullname.split()[1],
        relationship=relation,
        telephone="5926000000"
    )
    contact.patient.set([pat])

    return contact

def specialization():
    return Specialization.objects.create(
        name=fake.text(max_nb_chars=15)
    )
    


