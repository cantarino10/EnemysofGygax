# Generated by Django 4.2.16 on 2024-11-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.CharField(max_length=50)),
                ('BBA', models.CharField(max_length=10)),
                ('HitDice', models.IntegerField()),
                ('Saves', models.CharField(max_length=20)),
                ('Abilities', models.CharField(max_length=5000)),
                ('Skills', models.IntegerField()),
            ],
        ),
    ]
