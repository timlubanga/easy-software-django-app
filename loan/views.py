from django.shortcuts import render
from loan.models import Loan
from loan.serializers import LoanSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

customerModel = get_user_model()


class LoanCreateView(generics.GenericAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAdminUser]
    queryset = Loan.objects.all()

    def post(self, request, *args, **kwargs):
        customerid = kwargs.get('customerid', None)
        if customerid:
            try:
                customer = customerModel.objects.get(id=customerid)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND, data={'message': "the customer id is incorrect"})
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(customerId=customer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "please ensure the request has a customerid"})


class LoanListView(generics.ListAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]
    queryset = Loan.objects.all()

    def get_queryset(self):
        if Loan.objects.all().exists():
            queryset = Loan.objects.filter(customerId=self.request.user)
            return queryset
        else:
            return Loan.objects.all()


class RetrievUpdateLoanView(generics.RetrieveUpdateAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAdminUser]
    queryset = Loan.objects.all()
    
