# Generated by Django 3.2.4 on 2021-06-26 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('feedback', '0002_feedback_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student.student'),
        ),
    ]
