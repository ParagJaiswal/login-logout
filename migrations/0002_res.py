# Generated by Django 3.1.5 on 2021-02-28 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Res',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=12)),
                ('education', models.CharField(max_length=50)),
                ('fieldstudy', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('tpstartm', models.CharField(max_length=50)),
                ('tpstarty', models.CharField(max_length=50)),
                ('tpendm', models.CharField(max_length=50)),
                ('tpendy', models.CharField(max_length=50)),
                ('exptitle', models.CharField(max_length=100)),
                ('expcompany', models.CharField(max_length=100)),
                ('expstartm', models.CharField(max_length=100)),
                ('expstarty', models.CharField(max_length=100)),
                ('expendm', models.CharField(max_length=100)),
                ('expendy', models.CharField(max_length=100)),
            ],
        ),
    ]
