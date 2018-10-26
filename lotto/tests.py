from django.test import TestCase
from .models import GuessNumbers
class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(
            name='apple', text='pineapple', num_lotto=10)
        g.generate()
        print(g.update_date)
        print(g.lottos)
        self.assertTrue(len(g.lottos) < 5)