from django.urls import path
from loan.views import LoanCreateView, LoanListView


loanurlpatterns = [
    path('create/', LoanCreateView.as_view(), name="create"),
    path('list/', LoanListView.as_view(), name="list"),
]
