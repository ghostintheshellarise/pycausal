from unittest import TestCase

import pycausal

class TestJoke(TestCase):
    def test_is_graph(self):
        s = pycausal.backdoor()
        self.assertTrue(isinstance(s, basestring))
