from loan.tests.test_setUp import BaseTestSetup
from loan.models import Loan


class TestLoanView(BaseTestSetup):

    def test_user_cannot_create_loan_without_authentication(self):
        response = self.client.post(self.createOneUrl, format='json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            response.data['detail'], 'Authentication credentials were not provided.')

    def test_user_cannot_create_loan_without_admin_priviledges(self):

        response = self.client.post(
            self.createOneUrl, data=self.correctloanData, HTTP_AUTHORIZATION='Bearer {token}'.format(
                token=self.usertoken))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            response.data['detail'], 'You do not have permission to perform this action.')

    def test_admin_can_create_loan(self):
        url = str(self.createOneUrl).replace("3", "1")
        response = self.client.post(
            url, data=self.correctloanData, HTTP_AUTHORIZATION='Bearer {token}'.format(
                token=self.admintoken))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['customerId'], 1)

    def test_admin_cannot_create_loan_with_wrong_userId(self):
        response = self.client.post(
            self.createOneUrl, data=self.correctloanData, HTTP_AUTHORIZATION='Bearer {token}'.format(
                token=self.admintoken))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data['message'],
                         'the customer id is incorrect')
