# Generated by Django 4.2.17 on 2024-12-08 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alwayaApply', '0002_remove_application_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='company',
            field=models.ForeignKey(default=1, limit_choices_to={'role': 'company'}, on_delete=django.db.models.deletion.CASCADE, related_name='applications_as_company', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='application',
            name='freelancer',
            field=models.ForeignKey(limit_choices_to={'role': 'freelancer'}, on_delete=django.db.models.deletion.CASCADE, related_name='applications_as_freelancer', to=settings.AUTH_USER_MODEL),
        ),
    ]
