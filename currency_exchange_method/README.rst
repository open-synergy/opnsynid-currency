.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===============================
Currency Exchange Rate Inverted
===============================

This module has original name "currency_exchange_rate_inverted" from OCA Repository.
This module applies the inverse method in the conversion between two currencies.

The inverse method is a calculation method that uses the inverse (reciprocal)
exchange rate for the multiplier and divisor when converting amounts from one
currency to another.

The exchange rate of the multiplier and divisor are the reciprocal,
or opposite, of each other.

The inverse method multiplies the foreign amount by the
exchange rate to calculate the company currency (also called domestic) amount.

Configuration
=============

To convert amounts from one currency to another using the inverse method,
you have to go to 'Accounting / Configuration / Miscellaneous / Currencies'.
Then select the foreign currency that you wish to maintain inversion for
and set the flag 'Inverted exchange rate'.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/open-synergy/opnsynid-currency/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.


Credits
=======

Contributors
------------

* Eficent (www.eficent.com)
* Techrifiv Solutions Pte Ltd (www.techrifiv.com.sg)
* Statecraft Systems Pte Ltd (www.statecraftsystems.sg)
* Michael Viriyananda <viriyananda.michael@gmail.com>
* Andhitia Rama <andhitia.r@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id.com

This module is maintained by the PT. Simetri Sinergi Indonesia.
