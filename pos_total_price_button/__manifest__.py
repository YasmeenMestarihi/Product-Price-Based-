# -*- coding: utf-8 -*-
{
    'name': "POS Price-based Products",
    'version': "19.0.1.0.0",
    'summary': "Enter total price in POS; quantity is computed automatically for price-based products.",
    'description': """
        **Total Price button in POS**
        Adds a "Total Price" button to the Point of Sale control buttons. When the selected order line
        is for a price-based product, the cashier can enter the desired total amount; the system
        computes and sets the quantity (Qty = Total ÷ Unit Price). Unit price is never changed.

        **Per-product control**
        A boolean field "Price-based in POS" is added to the product form (Point of Sale tab).
        The Total Price button is only enabled when the selected line belongs to a product with
        this flag enabled. Invalid input, zero price, and missing selection are handled with
        clear alerts.
    """,
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
}
