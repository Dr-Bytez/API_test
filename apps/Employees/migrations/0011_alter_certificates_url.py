# Generated by Django 5.0.1 on 2024-02-03 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0010_alter_employee_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificates',
            name='url',
            field=models.URLField(max_length=1024),
        ),
    ]
