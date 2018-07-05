from atc53 import BaseAWSObject, AWSProperty


class WeightedItem(AWSProperty):
    props = {
        'EndpointReference': (basestring, False),
        'RuleReference': (basestring, False),
        'Weight': (basestring, True),
        'EvaluateTargetHealth': (bool, False),
        'HealthCheck': (basestring, False)
    }

    def validate(self):
        if not self.properties.get('Weight') in range(0, 255):
            raise ValueError('Weighted value not in range of 0-255')


class WeightedRule(BaseAWSObject):
    rule_type = 'weighted'
    props = {
        'Items': ([WeightedItem], True)
    }
