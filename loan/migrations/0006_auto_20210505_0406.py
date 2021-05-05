# Generated by Django 3.2.1 on 2021-05-05 04:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0005_auto_20210505_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loanCode',
            field=models.UUIDField(blank=True, default=uuid.UUID('647cff39-39c3-47c3-84a3-92f2912d01a8'), null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='transactionId',
            field=models.UUIDField(default=uuid.UUID('49b895c6-ad57-11eb-a5fa-485f990e81eb'), primary_key=True, serialize=False),
        ),
    ]
