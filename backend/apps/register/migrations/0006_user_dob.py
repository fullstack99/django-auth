# Generated by Django 3.0.2 on 2020-02-19 20:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_user_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]