# Generated by Django 3.2.13 on 2022-07-03 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('WORK', 'Work Experience'), ('EDUCATION', 'Education'), ('COURSE', 'Course')], default='WORK', max_length=10)),
                ('title', models.CharField(help_text='Job or course title.', max_length=100)),
                ('organisation', models.CharField(help_text='Workplace or university.', max_length=100)),
                ('order', models.PositiveIntegerField(default=1)),
                ('start_date', models.TextField(max_length=20)),
                ('end_date', models.TextField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='KeySkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('order', models.PositiveIntegerField(default=1)),
                ('current', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=20)),
                ('demo_url', models.URLField(blank=True, null=True)),
                ('git_url', models.URLField(blank=True, null=True)),
                ('image', models.FilePathField(path='/images')),
                ('order', models.PositiveIntegerField(default=1)),
                ('current', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExperiencePoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('order', models.PositiveIntegerField(default=1)),
                ('current', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.experience')),
            ],
        ),
    ]
