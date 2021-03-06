# Generated by Django 3.1.6 on 2021-05-31 04:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest', models.CharField(max_length=9)),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=100)),
                ('district', models.EmailField(max_length=150)),
                ('group', models.CharField(choices=[('A+', 'A+'), ('AB+', 'AB+'), ('B+', 'B+'), ('O+', 'O+'), ('A-', 'A-'), ('AB-', 'AB-'), ('B-', 'B-'), ('O-', 'O-')], default='A+', max_length=50)),
                ('province', models.CharField(choices=[('Benguela', 'Benguela'), ('Bié', 'Bié'), ('Bengo', 'Bengo'), ('Cabinda', 'Cabinda'), ('Cuando Cubango', 'Cuando Cubango'), ('Cuanza Norte', 'Cuanza Norte'), ('Cuanza Sul', 'Cuanza Sul'), ('Cunene', 'Cunene'), ('Huila', 'Huila'), ('Huambo', 'Huambo'), ('Lunda Norte', 'Lunda Norte'), ('Lunda Sul', 'Lunda Sul'), ('Luanda', 'Luanda'), ('Malanje', 'Malanje'), ('Moxico', 'Moxico'), ('Namibe', 'Namibe'), ('Uíge', 'Uíge'), ('Zaire', 'Zaire')], default='Bengo', max_length=50)),
                ('municipe', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('password', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
