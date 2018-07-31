=====
atc53
=====

.. image:: https://travis-ci.org/cloudtools/atc53.png?branch=master
    :target: https://travis-ci.org/cloudtools/atc53

About
=====

atc53 - library to create `AWS Route53 Traffic Policy Document`_ descriptions.

This library operates in a similar fashion to `troposphere`_ by aiming for
compatibility and familiarity when defining infrastructure.

Installation
============

atc53 can be installed using the pip distribution system for Python by issuing:

.. code:: sh

    $ pip install atc53

Examples
========

A simple example, showing a fail over rule between two load balancers:

.. code:: python

    from atc53 import PolicyDocument
    from atc53.endpoint import Endpoint
    from atc53.rule.failover import FailoverRule, Primary, Secondary

    p = PolicyDocument()
    main = Endpoint('MainEndpoint',
                    Type='elastic-load-balancer',
                    Value='elb-222222.us-west-1.elb.amazonaws.com')
    backup = Endpoint('BackupEndpoint',
                      Type='elastic-load-balancer',
                      Value='elb-111111.us-west-1.elb.amazonaws.com')
    rule = FailoverRule('TestFailoverRule',
                        Primary=Primary(
                            EndpointReference='MainEndpoint'),
                        Secondary=Secondary(
                            EndpointReference='BackupEndpoint')
                        )
    p.add_endpoint(main)
    p.add_endpoint(backup)
    p.add_rule(rule)
    print(p.to_json())


Licensing
=========

atc53 is licensed under the `BSD 2-Clause license`_.
See `LICENSE`_ for the full license text.

.. _`AWS Route53 Traffic Policy Document`: https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html
.. _`troposphere`: https://github.com/cloudtools/troposphere
.. _`BSD 2-Clause license`: https://opensource.org/licenses/BSD-2-Clause
.. _`LICENSE`: https://github.com/cloudtools/atc53/blob/master/LICENSE
