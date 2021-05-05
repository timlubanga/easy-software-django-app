from rest_framework.test import APITestCase
from django.urls import reverse
from userAuth.models import UserAccount


class BaseTestSetup(APITestCase):
    def setUp(self):
        self.loginUrl = reverse('login')
        self.signurl = reverse('register')
        self.listurl = reverse('list')
        self.retrieveOneUrl = reverse(
            'retrieve', kwargs={'pk': '3ddd1598-adab-11eb-a5fa-485f990e81eb'})
        self.createOneUrl = reverse('create', kwargs={'customerid': 3})
        self.userData = {
            "email": "test1@gmail.com",
            "username": "testuser1",
            "password": "1234567",
            "confirm_password": "1234567"
        }

        self.adminData = {
            'username': 'timlubanga',
            'password': 'timlubanga'
        }
        UserAccount.objects.create_superuser(
            username="timlubanga", password='timlubanga', email='timlubanga@gmail.com')

        resp = self.client.post(
            self.loginUrl, data=self.adminData, format='json')
        self.admintoken = resp.data['tokens']['access']
        response = self.client.post(
            self.signurl, data=self.userData, format='json')
        self.usertoken = response.data['tokens']['access']

        self.usertoken = response.data['tokens']['access']
        self.correctloanData = {
            "amount": 5000,
            "loanDueDate": "2021-12-12",
            "interest": 250
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
