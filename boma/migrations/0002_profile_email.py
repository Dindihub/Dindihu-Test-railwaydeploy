# Generated by Django 4.0.5 on 2022-06-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
