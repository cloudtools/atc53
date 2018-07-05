from atc53 import BaseAWSObject, AWSProperty


class GeoProximityItem(AWSProperty):
    props = {
        'EndpointReference': (basestring, False),
        'RuleReference': (basestring, False),
        'Region': (basestring, False),
        'Latitude': (basestring, False),
        'Longitude': (basestring, False),
        'Bias': (basestring, False),
        'EvaluateTargetHealth': (bool, False),
        'HealthCheck': (basestring, False)
    }


class GeoProximityRule(BaseAWSObject):
    rule_type = 'geoproximity'
    props = {
        'GeoproximityLocations': ([GeoProximityItem], True)
    }
