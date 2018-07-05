from atc53 import BaseAWSObject, AWSProperty


class MultivalueItem(AWSProperty):
    props = {
        'EndpointReference': (basestring, False),
        'HealthCheck': (basestring, False)
    }


class MultivalueRule(BaseAWSObject):
    rule_type = 'multivalue'
    props = {
        'Items': ([MultivalueItem], True)
    }
