# test_example.py

import unittest

class TestExample(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(1, 1)

    def test_another_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertEqual(2, 2)
