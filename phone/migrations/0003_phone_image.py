# Generated by Django 4.0.3 on 2022-03-31 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0002_phone_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.ImageField(null=True, upload_to='phones'),
        ),
    ]
