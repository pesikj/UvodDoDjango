# Generated by Django 4.0.1 on 2022-01-30 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.branch'),
        ),
    ]
