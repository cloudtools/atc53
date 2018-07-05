import re
import json
import types

valid_names = re.compile(r'^[a-zA-Z0-9]+$')


def encode_to_dict(obj):
    if hasattr(obj, 'to_dict'):
        # Calling encode_to_dict to ensure object is
        # normalised to a base dictionary all the way down.
        return encode_to_dict(obj.to_dict())
    elif isinstance(obj, (list, tuple)):
        new_lst = []
        for o in list(obj):
            new_lst.append(encode_to_dict(o))
        return new_lst
    elif isinstance(obj, dict):
        props = {}
        for name, prop in obj.items():
            props[name] = encode_to_dict(prop)

        return props
    # This is useful when dealing with external libs using
    # this format. Specifically awacs.
    elif hasattr(obj, 'JSONrepr'):
        return encode_to_dict(obj.JSONrepr())
    return obj


def recordtype_validator(value):
    valid_recordtypes = [
        'A',
        'AAAA',
        'CAA',
        'CNAME',
        'MX',
        'NAPTR',
        'NS',
        'PTR',
        'SOA',
        'SPF',
        'SRV',
        'TXT'
    ]
    if value not in valid_recordtypes:
        raise ValueError('% is not a valid value')
    return value


class BaseAWSObject(object):
    def __init__(self, name, **kwargs):
        self.name = name
        self.attributes = []
        # Cache the keys for validity checks
        self.propnames = self.props.keys()

        # unset/None is also legal
        if name and not valid_names.match(name):
            raise ValueError('Name not alphanumeric')

        # Create the list of properties set on this object by the user
        self.properties = {}
        dictname = getattr(self, 'dictname', None)
        if dictname:
            self.resource = {
                dictname: self.properties,
            }
        else:
            self.resource = self.properties
        if hasattr(self, 'rule_type') and self.rule_type is not None:
            self.resource['RuleType'] = self.rule_type
        self.__initialized = True

        # Now that it is initialized, populate it with the kwargs
        for k, v in kwargs.items():
            # Special case Resource Attributes
            if k in self.attributes:
                self.resource[k] = v
            else:
                self.__setattr__(k, v)

    def __getattr__(self, name):
        try:
            return self.properties.__getitem__(name)
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if '_BaseAWSObject__initialized' not in self.__dict__:
            return dict.__setattr__(self, name, value)
        elif name in self.propnames:
            # Check the type of the object and compare against what we were
            # expecting.
            expected_type = self.props[name][0]

            # If the value is a AWSHelperFn we can't do much validation
            # we'll have to leave that to Amazon.  Maybe there's another way
            # to deal with this that we'll come up with eventually
            if isinstance(value, AWSHelperFn):
                return self.properties.__setitem__(name, value)

            # If it's a function, call it...
            elif isinstance(expected_type, types.FunctionType):
                value = expected_type(value)
                return self.properties.__setitem__(name, value)

            # If it's a list of types, check against those types...
            elif isinstance(expected_type, list):
                # If we're expecting a list, then make sure it is a list
                if not isinstance(value, list):
                    self._raise_type(name, value, expected_type)

                # Iterate over the list and make sure it matches our
                # type checks
                for v in value:
                    if not isinstance(v, tuple(expected_type)):
                        self._raise_type(name, v, expected_type)
                # Validated so assign it
                return self.properties.__setitem__(name, value)

            # Single type so check the type of the object and compare against
            # what we were expecting. Special case AWS helper functions.
            elif isinstance(value, expected_type):
                return self.properties.__setitem__(name, value)
            else:
                self._raise_type(name, value, expected_type)

        raise AttributeError('%s object does not support attribute %s' %
                             (self.type, name))

    def _raise_type(self, name, value, expected_type):
        raise TypeError('%s is %s, expected %s' %
                        (name, type(value), expected_type))

    def validate(self):
        pass

    def JSONrepr(self):
        for k, (prop_type, required) in self.props.items():
            if required and k not in self.properties:
                type = getattr(self, 'type', '<unknown type>')
                raise ValueError('Resource %s required in type %s' % (k, type))
        self.validate()
        # If no other properties are set, only return the Type.
        # Mainly used to not have an empty "Properties".
        if self.properties:
            return self.resource
        else:
            return {'Type': self.type}


class AWSHelperFn(object):
    @staticmethod
    def getdata(data):
        if isinstance(data, BaseAWSObject):
            return data.name
        else:
            return data


class AWSProperty(BaseAWSObject):
    dictname = None

    def __init__(self, title=None, **kwargs):
        super(AWSProperty, self).__init__(title, **kwargs)


class PolicyDocument(object):

    def __init__(self):  # noqa: N803
        self.record_type = None
        self.start_endpoint = None
        self.start_rule = None
        self.endpoints = {}
        self.rules = {}
        self.version = '2015-10-01'

    def to_dict(self):
        t = {}
        if self.start_endpoint:
            t['StartEndpoint'] = self.start_endpoint
        if self.start_rule:
            t['StartRule'] = self.start_rule
        if self.endpoints:
            t['Endpoints'] = self.endpoints
        if self.record_type:
            t['RecordType'] = self.record_type
        if self.rules:
            t['Rules'] = self.rules
        if self.version:
            t['AWSPolicyFormatVersion'] = self.version

        return encode_to_dict(t)

    def add_endpoint(self, endpoint):
        self.endpoints[endpoint.name] = endpoint

    def add_record_type(self, record_type):
        self.record_type = recordtype_validator(record_type)

    def add_rule(self, rule):
        self.rules[rule.name] = rule

    def add_start_endpoint(self, start_endpoint):
        self.start_endpoint = start_endpoint

    def add_start_rule(self, start_rule):
        # TODO: validate this rule exists already?
        self.start_rule = start_rule

    def add_version(self, version=None):
        if version:
            self.version = version
        else:
            self.version = '2015-10-01'

    def to_json(self, indent=4, sort_keys=True, separators=(',', ': ')):
        return json.dumps(self.to_dict(), indent=indent,
                          sort_keys=sort_keys, separators=separators)
