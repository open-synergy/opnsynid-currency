# -*- coding: utf-8 -*-
# Copyright 2015 Eficent
# Copyright 2015 Techrifiv Solutions Pte Ltd
# Copyright 2015 Statecraft Systems Pte Ltd
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models


class ResCurrency(models.Model):
    _inherit = "res.currency"

    rate_inverted = fields.Boolean(
        string="Inverted exchange rate",
    )

    @api.model
    def _get_conversion_rate(self, from_currency, to_currency):
        _super = super(ResCurrency, self)
        res = _super._get_conversion_rate(from_currency, to_currency)

        if (
            from_currency.rate_inverted
            and to_currency.rate_inverted
            or not from_currency.rate_inverted
            and not to_currency.rate_inverted
        ):
            return res
        else:
            return 1 / res
