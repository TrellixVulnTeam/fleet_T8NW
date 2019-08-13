# Generated by Django 2.0.6 on 2019-08-11 19:30

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
            name='AddDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Driver_Name', models.CharField(max_length=10)),
                ('Vehicle_Number', models.CharField(max_length=10)),
                ('Sim_Number', models.CharField(max_length=10)),
                ('IMEI_Number', models.CharField(max_length=10)),
                ('Device_Model', models.CharField(choices=[('P', 'Prime 07'), ('B', 'Benley 140'), ('O', 'OBDII'), ('R', 'Optimus 2.0')], max_length=20)),
                ('Vehicle_Licence_No', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(default='my_company', max_length=10, null=True)),
                ('Company_address', models.TextField(default='my_company', max_length=50, null=True)),
                ('Phone_number', models.CharField(default='my_company', max_length=10, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]