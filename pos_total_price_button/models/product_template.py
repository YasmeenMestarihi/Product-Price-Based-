# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    pos_price_based = fields.Boolean(
        string="Price-based in POS",
        help="When enabled, cashiers can enter the total price for this product in POS instead of unit price and quantity.",
        default=False,
    )
