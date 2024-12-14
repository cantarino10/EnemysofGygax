# Generated by Django 4.2.16 on 2024-11-02 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='Reach',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='race',
            name='Size',
            field=models.CharField(default='Medium', max_length=10),
        ),
        migrations.AlterField(
            model_name='race',
            name='SkillBonus',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='Space',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='race',
            name='Speed',
            field=models.IntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='race',
            name='level_adjstument',
            field=models.IntegerField(default=0),
        ),
    ]