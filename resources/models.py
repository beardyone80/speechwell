from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class Specialty(models.Model):
    SPECIALTY_CHOICES = [
        ('Apraxia of Speech', 'Apraxia of Speech'),
        ('Stuttering – Stammering', 'Stuttering – Stammering'),
        ('Dysarthria', 'Dysarthria'),
        ('Lisping', 'Lisping'),
        ('Spasmodic Dysphonia', 'Spasmodic Dysphonia'),
        ('Developmental Language Disorder', 'Developmental Language Disorder'),
        ('Muteness – Selective Mutism', 'Muteness – Selective Mutism'),
        ('Aphasia', 'Aphasia'),
        ('Speech Delay', 'Speech Delay'),
    ]
    
    name = models.CharField(max_length=100, choices=SPECIALTY_CHOICES)

    def __str__(self):
        return self.name

class Therapist(models.Model):
    LOCATION_CHOICES = [
        ('Scotland', 'Scotland'),
        ('North', 'North'),
        ('Midlands', 'Midlands'),
        ('South', 'South'),
        ('Wales', 'Wales'),
    ]

    therapistID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    profile_pic = models.ImageField(
        storage=RawMediaCloudinaryStorage(),
        blank=True,
        null=True
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    specialty = models.ManyToManyField(Specialty)  # Many-to-many relationship with Specialty model

    def __str__(self):
        return self.username
