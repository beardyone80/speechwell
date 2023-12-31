# Generated by Django 4.2.7 on 2023-12-03 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_alter_therapist_bio'),
        ('disorders', '0004_disorder_created_on_disorder_excerpt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.therapist')),
                ('disorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='disorders.disorder')),
            ],
        ),
    ]
