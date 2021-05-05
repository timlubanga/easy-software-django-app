from django.urls import path
from loan.views import LoanCreateView, LoanListView, RetrievUpdateLoanView


loanurlpatterns = [
    path('<customerid>/create/', LoanCreateView.as_view(), name="create"),
    path('list/', LoanListView.as_view(), name="list"),
    path('retrieve/<pk>', RetrievUpdateLoanView.as_view(), name="retrieve"),
]
