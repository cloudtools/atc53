from atc53 import PolicyDocument
from atc53.rule.weighted import WeightedItem, WeightedRule

import unittest


class TestWeightedRule(unittest.TestCase):
    def test_invalid_weight_rule(self):
        weighted_rule = WeightedRule('TestWeightedRule', Items=[
            WeightedItem(
                Weight='9001'
            )
        ])

        p = PolicyDocument()
        p.add_rule(weighted_rule)
        with self.assertRaises(ValueError):
            p.to_json()
