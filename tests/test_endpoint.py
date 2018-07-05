from atc53.endpoint import Endpoint

import unittest


class TestEndpoint(unittest.TestCase):
    def test_bad_endpoint(self):
        with self.assertRaises(ValueError):
            Endpoint('Endpoint', Type='invalidtype')
