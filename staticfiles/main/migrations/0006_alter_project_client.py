# Generated by Django 4.1.7 on 2023-03-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.CharField(max_length=255),
        ),
    ]
