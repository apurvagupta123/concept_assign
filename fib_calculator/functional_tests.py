from django.test import TestCase


class TestFibCalculator(TestCase):
    def test_fib_input(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_cal_fib(self):
        response = self.client.post('/output', {'num_field': 9})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Fib num is: 34')
