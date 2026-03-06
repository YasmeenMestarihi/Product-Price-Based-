# -*- coding: utf-8 -*-
import os

with open(
    os.path.join(os.path.dirname(__file__), "static", "description", "index.html"),
    encoding="utf-8",
) as f:
    _description_html = f.read()

__manifest__ = {
    'name': "POS Price-based Products",
    'version': "19.0.1.0.0",
    'summary': "Enter total price in POS; quantity is computed automatically for price-based products.",
    'description': _description_html,
    'category': "Point of Sale",
    'icon': '/pos_total_price_button/static/description/icon.png',
    'author': "Yasmeen Mestarihi",
    'license': "LGPL-3",
    'depends': ["point_of_sale", "product"],
    'data': [
        "views/product_template_view.xml",
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_total_price_button/static/src/js/pos_total_price_button.js',
            'pos_total_price_button/static/src/xml/pos_total_price_button.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 200,
    'currency': 'USD',
}
