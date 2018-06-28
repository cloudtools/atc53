from . import BaseAWSObject


def validate_rule_type(value):
    valid_rule_types = [
        'failover',
        'geo',
        'geoproximity',
        'latency',
        'multivalue',
        'weighted'
    ]
    if value not in valid_rule_types:
        raise ValueError('% is not a valid value for Rule')
    return value


class Rule(BaseAWSObject):
        props = {
            'RuleType': (validate_rule_type, True),
            'EndpointReference ': (basestring, False),
            'RuleReference': (basestring, False),
            'EvaluateTargetHealth': (bool, False),
            'HealthCheck': (basestring, False),
            'GeoproximityLocations': (object, False)
        }

        def validate(self):
            pass
