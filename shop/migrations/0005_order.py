# Generated by Django 4.0.6 on 2022-07-24 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_contact_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=400)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
            ],
        ),
    ]
