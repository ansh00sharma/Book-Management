# Generated by Django 4.2.7 on 2023-11-29 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='book_table',
            fields=[
                ('book_name', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('author_id', models.CharField(max_length=5)),
                ('stock', models.IntegerField()),
                ('Added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_table',
            fields=[
                ('user_email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('user_password', models.CharField(max_length=256)),
                ('user_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
