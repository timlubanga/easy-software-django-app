# Generated by Django 3.2.1 on 2021-05-05 03:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0003_auto_20210505_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loanCode',
            field=models.UUIDField(blank=True, default=uuid.UUID('4bba764f-dfa0-4b0e-b231-e99329070d33'), null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='transactionId',
            field=models.UUIDField(default=uuid.UUID('dc010c9c-ad52-11eb-a5fa-485f990e81eb'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
