# Generated by Django 5.2 on 2025-04-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('smtp_server', models.CharField(max_length=255)),
                ('smtp_email', models.CharField(max_length=255)),
                ('smtp_password', models.CharField(max_length=255)),
                ('smtp_port', models.CharField(max_length=255)),
                ('youtube', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='setting/')),
                ('aboutus', models.TextField()),
                ('contact', models.TextField()),
            ],
        ),
    ]
