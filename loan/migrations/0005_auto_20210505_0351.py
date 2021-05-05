# Generated by Django 3.2.1 on 2021-05-05 03:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_auto_20210505_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loanCode',
            field=models.UUIDField(blank=True, default=uuid.UUID('cf199d7e-547a-4722-bbc6-0618f80aeafb'), null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='transactionId',
            field=models.UUIDField(default=uuid.UUID('27ba4b88-ad55-11eb-a5fa-485f990e81eb'), editable=False, primary_key=True, serialize=False),
        ),
    ]
