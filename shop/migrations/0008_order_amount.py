# Generated by Django 4.0.6 on 2022-07-30 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_rename_timestamp_orderupdate_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]