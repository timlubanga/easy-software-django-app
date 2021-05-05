from django.contrib import admin
from django.conf import settings
from loan.models import Loan


class LoanAdmin(admin.ModelAdmin):
    list_display = ['transactionId', 'amount',
                    'interest', "customerId", 'loanCode']


admin.site.register(Loan, LoanAdmin)
