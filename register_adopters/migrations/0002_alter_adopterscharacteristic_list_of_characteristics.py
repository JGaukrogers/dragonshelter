# Generated by Django 4.0.6 on 2022-07-27 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_adopters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adopterscharacteristic',
            name='list_of_characteristics',
            field=models.ManyToManyField(blank=True, to='register_adopters.adopter'),
        ),
    ]
