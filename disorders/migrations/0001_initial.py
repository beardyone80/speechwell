# Generated by Django 4.2.7 on 2023-12-03 17:32

import cloudinary_storage.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resources', '0003_alter_therapist_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disorder',
            fields=[
                ('disorderID', models.AutoField(primary_key=True, serialize=False)),
                ('profile_pic', models.ImageField(blank=True, null=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='')),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.therapist')),
                ('disorder_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.specialty')),
            ],
        ),
    ]
