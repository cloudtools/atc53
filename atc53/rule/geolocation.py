from atc53 import BaseAWSObject, AWSProperty


class GeoLocationItem(AWSProperty):
    props = {
        'EndpointReference': (basestring, False),
        'RuleReference': (basestring, False),
        'IsDefault': (bool, False),
        'Continent': (basestring, False),
        'Country': (basestring, False),
        'Subdivision': (basestring, False),
        'EvaluateTargetHealth': (bool, False),
        'HealthCheck': (basestring, False)
    }


class GeolocationRule(BaseAWSObject):
    rule_type = 'geo'
    props = {
        'Location': ([GeoLocationItem], True)
    }
