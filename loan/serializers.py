from rest_framework import serializers
from loan.models import Loan


class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = ['amount', 'interest', 'customerId',
                  'loanCode',  'loanDate', 'loanDueDate']
        extra_kwargs = {'loanCode': {'read_only': True}}
