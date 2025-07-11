# Generated by Django 5.2 on 2025-05-16 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_courselang_subjectlang_tutorlang'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorlang',
            name='lang',
            field=models.CharField(choices=[('en', 'English'), ('uz', "O'zbekcha"), ('ru', 'Русский')], default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutorlang',
            name='seting',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.subject'),
            preserve_default=False,
        ),
    ]
