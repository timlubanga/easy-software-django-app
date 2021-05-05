from django.shortcuts import render
from loan.models import Loan
from loan.serializers import LoanSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.


class LoanCreateView(generics.CreateAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]
    queryset = Loan.objects.all()

    def perform_create(self, serializer):
        serializer.save(customerId=self.request.user)


class LoanListView(generics.ListAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]
    queryset = Loan.objects.all()

    def get_queryset(self):
        if Loan.objects.all().exists():
            queryset = Loan.objects.all(customerId=self.request.user)
            return queryset
        else:
            return Loan.objects.all()
