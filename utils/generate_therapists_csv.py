import django
import os
import sys
from pathlib import Path
from faker import Faker
import csv
import random

def setup_django_environment():
    # Change 'project_name' to your Django project's name
    project_path = Path('speechwell')
    sys.path.append(str(project_path))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'speechwell.settings'
    django.setup()

def generate_therapists_csv():
    from resources.models import Therapist, Specialty
    
    # Create a list of specialty choices
    SPECIALTY_CHOICES = [
        'Apraxia of Speech', 'Stuttering – Stammering', 'Dysarthria', 'Lisping',
        'Spasmodic Dysphonia', 'Developmental Language Disorder', 'Muteness – Selective Mutism',
        'Aphasia', 'Speech Delay'
    ]

    # Check and create specialties in the database if they don't exist
    for specialty_name in SPECIALTY_CHOICES:
        Specialty.objects.get_or_create(name=specialty_name)

    fake = Faker()
    therapists = []
    for _ in range(30):
        therapist = {
            'username': fake.user_name(),
            'email': fake.email(),
            'phone_number': fake.phone_number(),
            'address': fake.address(),
            'bio': fake.text(max_nb_chars=500),
            'location': random.choice(['Scotland', 'North', 'Midlands', 'South', 'Wales']),
            # Generate random number of specialties per therapist
            'specialty': ', '.join(random.sample(SPECIALTY_CHOICES, random.randint(1, len(SPECIALTY_CHOICES))))
        }
        therapists.append(therapist)

    filename = 'therapists.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['username', 'email', 'phone_number', 'address', 'bio', 'location', 'specialty']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for therapist in therapists:
            writer.writerow(therapist)

    print(f"Therapists data saved to {filename}")

if __name__ == "__main__":
    setup_django_environment()
    generate_therapists_csv()
