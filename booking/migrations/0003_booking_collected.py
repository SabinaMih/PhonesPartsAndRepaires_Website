# Generated by Django 3.1.7 on 2021-03-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20210305_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='collected',
            field=models.BooleanField(default=False),
        ),
    ]