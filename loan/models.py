from django.db import models
import uuid
# Create your models here.
from django.contrib.auth import get_user_model

Customer = get_user_model()


class Loan(models.Model):
    transactionId = models.UUIDField(primary_key=True, unique=True,
                                     default=uuid.uuid1)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    interest = models.DecimalField(decimal_places=2, max_digits=10)
    loanCode = models.UUIDField(null=True, blank=True,
                                default=uuid.uuid4())
    loanDate = models.DateTimeField(auto_now_add=True)
    loanDueDate = models.DateField(null=False, blank=False)
    customerId = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.amount)
