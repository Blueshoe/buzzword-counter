# Generated by Django 2.2.12 on 2020-04-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("counter", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="buzzword",
            options={"ordering": ["word"]},
        ),
        migrations.AlterField(
            model_name="buzzword",
            name="word",
            field=models.CharField(max_length=127, unique=True),
        ),
    ]
