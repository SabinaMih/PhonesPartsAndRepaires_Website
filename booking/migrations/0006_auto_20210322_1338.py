# Generated by Django 3.1.7 on 2021-03-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_merge_20210322_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='count_bookings',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
