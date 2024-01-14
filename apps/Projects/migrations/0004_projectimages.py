# Generated by Django 5.0.1 on 2024-01-14 19:16

import apps.Projects.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0003_alter_project_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=apps.Projects.models.image_directory_path)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.project')),
            ],
        ),
    ]
