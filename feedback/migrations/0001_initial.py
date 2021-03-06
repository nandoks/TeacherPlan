# Generated by Django 3.2.4 on 2021-06-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_steps', models.TextField(blank=True)),
                ('homework_link', models.TextField(blank=True)),
                ('greeting', models.TextField(blank=True)),
                ('lexis', models.TextField(blank=True)),
                ('corrections', models.TextField(blank=True)),
                ('summary', models.TextField(blank=True)),
                ('praise', models.TextField(blank=True)),
                ('teacher_only', models.TextField(blank=True)),
            ],
        ),
    ]
