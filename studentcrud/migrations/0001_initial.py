# Generated by Django 3.1.1 on 2020-09-09 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_id', models.CharField(max_length=10)),
                ('stud_name', models.CharField(max_length=50)),
                ('stud_email', models.EmailField(max_length=254)),
                ('stud_contact', models.CharField(max_length=15)),
            ],
        ),
    ]
