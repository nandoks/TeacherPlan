# Generated by Django 3.2.4 on 2021-06-26 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lesson', '0001_initial'),
        ('lesson_plan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lesson_plan.lessonplan'),
        ),
    ]
