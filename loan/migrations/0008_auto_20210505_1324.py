# Generated by Django 3.2.1 on 2021-05-05 13:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0007_auto_20210505_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loanCode',
            field=models.UUIDField(blank=True, default=uuid.UUID('c38978de-7246-4eba-86ec-b449883e272b'), null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loanDueDate',
            field=models.DateField(),
        ),
    ]
