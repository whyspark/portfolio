# Generated by Django 3.2.13 on 2022-07-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220703_1340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ['type', 'order']},
        ),
        migrations.AlterModelOptions(
            name='experiencepoint',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='keyskill',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
