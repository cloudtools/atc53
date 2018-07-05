from atc53 import BaseAWSObject, AWSProperty


class LatencyItem(AWSProperty):
    props = {
        'EndpointReference': (basestring, False),
        'RuleReference': (basestring, False),
        'Region': (basestring, False),
        'EvaluateTargetHealth': (bool, False),
        'HealthCheck': (basestring, False)
    }


class LatencyRule(BaseAWSObject):
    rule_type = 'latency'
    props = {
        'Regions': ([LatencyItem], True)
    }
