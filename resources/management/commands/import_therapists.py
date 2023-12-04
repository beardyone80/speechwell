from django.core.management.base import BaseCommand
from resources.models import Therapist
import csv

class Command(BaseCommand):
    help = 'Imports therapists from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Create Therapist objects from CSV data and save them
                therapist = Therapist(
                    username=row['username'],
                    email=row['email'],
                    phone_number=row['phone_number'],
                    address=row['address'],
                    bio=row['bio'],
                    location=row['location'],
                    # Parse and assign specialty appropriately to Therapist objects
                    # This might require additional processing based on how you've saved specialties in the CSV
                )
                therapist.save()

        self.stdout.write(self.style.SUCCESS('Therapists imported successfully'))
