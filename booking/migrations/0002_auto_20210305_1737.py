# Generated by Django 3.1.7 on 2021-03-05 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-created', 'booking_date']},
        ),
        migrations.AddField(
            model_name='booking',
            name='arrived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='comment',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='booking',
            name='repaired',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='count_bookings',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
