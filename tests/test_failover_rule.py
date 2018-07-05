from atc53 import PolicyDocument
from atc53.rule.failover import FailoverRule, Primary, Secondary

import unittest


class TestFailoverRule(unittest.TestCase):
    def test_missing_secondary_rule(self):
        failover_rule = FailoverRule('TestFailoverRule',
                                     Primary=Primary(EndpointReference='MissingEndpoint'))

        p = PolicyDocument()
        p.add_rule(failover_rule)
        with self.assertRaises(ValueError):
            p.to_json()

    def test_both_rules(self):
        failover_rule = FailoverRule('TestFailoverRule',
                                     Primary=Primary(EndpointReference='MissingEndpoint'),
                                     Secondary=Secondary(EndpointReference='MissingEndpoint')
                                     )
        p = PolicyDocument()
        p.add_rule(failover_rule)
