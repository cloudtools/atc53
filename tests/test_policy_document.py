from atc53 import PolicyDocument

import unittest


class TestPolicyDocument(unittest.TestCase):
    def test_invalid_record_type(self):
        p = PolicyDocument()
        with self.assertRaises(ValueError):
            p.add_record_type('B')
