# Generated by Django 3.1.6 on 2021-07-02 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_donor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
