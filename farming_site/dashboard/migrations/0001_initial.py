# Generated by Django 5.1.3 on 2024-11-30 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=280)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
