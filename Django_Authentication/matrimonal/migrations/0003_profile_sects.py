# Generated by Django 4.2.14 on 2024-09-03 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("matrimonal", "0002_caste_fatherprofile_hobby_religion_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="sects",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profiles",
                to="matrimonal.sects",
            ),
        ),
    ]
