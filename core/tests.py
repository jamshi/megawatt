from django.test import TestCase
from core.models import Site

SUMMARY_SUM_RESULT = {1: (52.00, 196.00),
                      2: (5.00, 15.00),
                      3: (10.00, 30.00)}

SUMMARY_AVG_RESULT = {1: (17.33, 65.33),
                      2: (5.00, 15.00),
                      3: (5.00, 15.00)}

class SummaryTestCase(TestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        pass
        # Test definitions as before.
        # call_setup_methods()

    def test_summary_sum(self):
        summary = Site.objects.get_sum_grouped()
        for x in summary:
            self.assertEqual(round(x.a_value_sum, 2), SUMMARY_SUM_RESULT[x.id][0])
            self.assertEqual(round(x.b_value_sum, 2), SUMMARY_SUM_RESULT[x.id][1])

    
    def test_summary_avg(self):
        summary = Site.objects.get_average_grouped()
        for x in summary:
            self.assertEqual(round(x.a_value_avg, 2), SUMMARY_AVG_RESULT[x.id][0])
            self.assertEqual(round(x.b_value_avg, 2), SUMMARY_AVG_RESULT[x.id][1])
        # A test that uses the fixtures.
        # call_some_test_code()