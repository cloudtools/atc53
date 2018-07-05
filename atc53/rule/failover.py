from atc53 import AWSProperty, BaseAWSObject


class Primary(AWSProperty):
    # FIXME these should not be separate classes
    props = {
        'HealthCheck': (basestring, False),
        'EvaluateTargetHealth': (bool, False),
        'EndpointReference': (basestring, False),
        'RuleReference': (basestring, False)
    }


class Secondary(AWSProperty):
    props = {
        'HealthCheck': (basestring, False),
        'EvaluateTargetHealth': (bool, False),
        'EndpointReference': (basestring, False),
        'RuleReference': (basestring, False)
    }


class FailoverRule(BaseAWSObject):
    rule_type = "failover"

    props = {
        'Primary': (Primary, True),
        'Secondary': (Secondary, True)
    }
