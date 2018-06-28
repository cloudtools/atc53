from tpd.rule import Rule

import unittest


class TestRule(unittest.TestCase):
    def test_bad_rule(self):
        with self.assertRaises(ValueError):
            Rule('Rule', RuleType='invalidtype')