from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Specialty model


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

# Therapist model including location choices
# linked to specialty model many-to-many


class Therapist(models.Model):
    LOCATION_CHOICES = [
        ('Scotland', 'Scotland'),
        ('North', 'North'),
        ('Midlands', 'Midlands'),
        ('South', 'South'),
        ('Wales', 'Wales'),
    ]

    therapistID = models.AutoField(primary_key=True)
    username = models.CharField(
        max_length=100, help_text="Enter the name you wish"
        "to be displayed as in the directory, this can include spaces."
        )
    email = models.EmailField(
        blank=True, null=True,
        help_text=("(Optional) Enter an email where"
                   "clients can contact you")
        )
    profile_pic = models.ImageField(
        storage=RawMediaCloudinaryStorage(),  # Uses cloudinary storage
        blank=True,
        null=True,
        help_text=(
            "(Optional) Upload a profile picture or your business logo;"
            "all pictures will be automatically resized."
            )
        )
    phone_number = models.CharField(
        max_length=20, blank=True, null=True,
        help_text="(Optional) Enter your business phone number."
        )
    address = models.TextField(
        blank=True, null=True, help_text=(
            "(Optional) Enter your practice/business address"
            )
        )
    bio = models.TextField(
        max_length=500, blank=True, null=True,
        help_text=(
            "(Optional) Enter a short biography/description of yourself or"
            "your business; max length 500 characters"
            )
        )
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    specialty = models.ManyToManyField(
        Specialty, help_text=(
            "To select more than one please hold the CTRL key on your keyboard"
            "as you select them (mobile users can select using the checkboxes)"
        )  # Many-to-many relationship with Specialty model
    )

    def __str__(self):
        return self.username
