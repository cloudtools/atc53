===
tpd
===

About
=====

tpd - library to create `AWS Route53 Traffic Policy Document`_ descriptions.
This library operates in a similar fashion to `troposphere`_ , aiming for
compatibility and familiarity when defining infrastructure.

Installation
============

As this code is not yet published to pypi, please use pip to install from
Github:

.. code:: sh

    $ pip install git+ssh://git@github.com/tigertoes/tpd

Examples
========

A simple example:

.. code:: python

    from tpd import PolicyDocument
    import tpd.rule as rule

    p = PolicyDocument()

Licensing
=========

tpd is licensed under the `BSD 2-Clause license`_.
See `LICENSE`_ for the full license text.

.. _`AWS Route53 Traffic Policy Document`: https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html
.. _`troposphere`: https://github.com/cloudtools/troposphere
.. _`BSD 2-Clause license`: https://opensource.org/licenses/BSD-2-Clause
.. _`LICENSE`: https://github.com/tigertoes/tpd/blob/master/LICENSE
