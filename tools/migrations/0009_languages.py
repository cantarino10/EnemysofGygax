# Generated by Django 4.2.16 on 2024-11-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0008_carrying_str'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30)),
                ('speakers', models.CharField(max_length=100)),
                ('Alphabet', models.CharField(max_length=20)),
            ],
        ),
    ]