# Generated by Django 4.1.7 on 2023-03-02 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=30)),
            ],
        ),
    ]
