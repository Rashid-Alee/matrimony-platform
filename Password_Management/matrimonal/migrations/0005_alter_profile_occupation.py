# Generated by Django 4.2.14 on 2024-09-03 20:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("matrimonal", "0004_alter_hobby_options_alter_sects_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="occupation",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
