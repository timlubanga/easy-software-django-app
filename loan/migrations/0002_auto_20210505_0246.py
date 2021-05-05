# Generated by Django 3.2.1 on 2021-05-05 02:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='interest',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loanCode',
            field=models.UUIDField(blank=True, default=uuid.UUID('e6d72201-e53e-4144-9705-ba49e07560df'), null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='transactionId',
            field=models.UUIDField(default=uuid.UUID('3f8ee92b-4b88-4a3a-866d-55b0205741be'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
