# Generated by Django 3.0.1 on 2020-04-24 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sub1', models.IntegerField()),
                ('sub2', models.IntegerField()),
                ('sub3', models.IntegerField()),
                ('sub4', models.IntegerField()),
                ('sub5', models.IntegerField()),
                ('Dob', models.DateField(blank=True, null=True)),
            ],
        ),
    ]