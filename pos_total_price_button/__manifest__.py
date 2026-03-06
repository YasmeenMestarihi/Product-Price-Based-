# -*- coding: utf-8 -*-
{
    'name': "POS Price-based Products",
    'version': "19.0.1.0.0",
    'summary': "Enter total price in POS; quantity is computed automatically for price-based products.",
    'description': """
<div class="oe_module_desc">
    <p>
        <strong>Why this module?</strong> When customers ask for an amount in money (e.g. &quot;I want 5 JOD of grapes&quot;) instead of a quantity, the cashier can enter the <strong>total price</strong> directly. The system calculates the quantity automatically - no mental math, correct inventory and invoicing.
    </p>
    <p><strong>Key benefits:</strong></p>
    <ul>
        <li>Sell by total amount (e.g. 10.00) instead of quantity - ideal for weighed products, bakery, deli.</li>
        <li>Per-product control: enable &quot;Price-based in POS&quot; only for the products that need it.</li>
        <li>Unit price stays fixed; only quantity is updated. Inventory and financial movements remain accurate.</li>
    </ul>

    <h2>Total Price button in POS</h2>
    <p>
        Adds a <strong>Total Price</strong> button to the Point of Sale control buttons. When the selected order line
        is for a price-based product, the cashier can enter the desired total amount; the system
        computes and sets the quantity (Qty = Total / Unit Price). Unit price is never changed.
    </p>

    <h2>Per-product control</h2>
    <p>
        A boolean field <strong>Price-based in POS</strong> is added to the product form (Point of Sale tab).
        The Total Price button is only enabled when the selected line belongs to a product with
        this flag enabled. Invalid input, zero price, and missing selection are handled with
        clear alerts.
    </p>
    <p>
        <img src="product-price-based-field.png" alt="Product form: Point of Sale tab with Price-based in POS enabled" class="img-fluid" style="max-width: 100%;"/>
    </p>
    <p class="text-muted"><em>Product form - Point of Sale tab: enable "Price-based in POS" for the product. The Total Price button in POS is then available for this product.</em></p>
    <p>
        <img src="product-without-price-based-field.png" alt="Product form: Price-based in POS disabled - Total Price button not available for this product in POS" class="img-fluid" style="max-width: 100%;"/>
    </p>
    <p class="text-muted"><em>Product with "Price-based in POS" disabled: in POS the Total Price button stays disabled for this product; only products with the field enabled can use it.</em></p>

    <h2>Requirements</h2>
    <ul>
        <li><strong>Odoo 19</strong> (Community or Enterprise)</li>
        <li><strong>Point of Sale</strong> app installed and used in your database</li>
    </ul>

    <h2>How it works</h2>
    <ol>
        <li>In the product form, open the <strong>Point of Sale</strong> tab. Enable the <strong>Price-based in POS</strong> checkbox (below "Is a Weighed Product?").</li>
        <li>In the POS session, add that product to the order and select its order line.</li>
        <li>The <strong>Total Price</strong> button in the control-buttons area becomes clickable.</li>
        <li>Click <strong>Total Price</strong>. Enter the desired total (e.g. <code>2</code>). The system computes: <strong>Qty = EnteredTotal / UnitPrice</strong>.</li>
        <li>The order line quantity is updated; unit price and line total reflect the entered amount.</li>
    </ol>
    <p>
        <img src="pos-total-price-button-enabled.png" alt="POS with price-based product selected: Total Price button enabled" class="img-fluid" style="max-width: 100%;"/>
    </p>
    <p class="text-muted">
        <em>Step 1: Select the product (with the field enabled). Step 2: Click <strong>Total Price</strong>. The button is enabled for price-based products.</em>
    </p>
    <p>
        <img src="pos-enter-total-price-popup.png" alt="Total Price popup: Enter total price" class="img-fluid" style="max-width: 100%;"/>
    </p>
    <p class="text-muted">
        <em>Step 3: A popup appears - <strong>Enter total price:</strong> Type the amount (e.g. <strong>5</strong>) and click <strong>OK</strong>. The system will update the line quantity automatically.</em>
    </p>
    <p>
        <img src="pos-total-price-success.png" alt="Success: quantity and total updated" class="img-fluid" style="max-width: 100%;"/>
    </p>
    <p class="text-muted">
        <em>Step 4: A <strong>Success</strong> message appears with the calculated quantity and total. The order line is updated (e.g. 0.42 Apple Pie, 5.00 total). This operation generates the corresponding <strong>inventory</strong> and <strong>financial</strong> movements in Odoo.</em>
    </p>
    <p>
        <img src="pos-total-price-final-result.png" alt="Final result: order line with calculated quantity and total" class="img-fluid" style="max-width: 100%;"/>
    </p>
    <p class="text-muted">
        <em><strong>Final result:</strong> The order shows 0.42 Apple Pie with total 5.80 (including taxes). The product card displays the quantity (0.42). The line is ready for payment.</em>
    </p>
    <p>
        <img src="pos-total-price-button-disabled-non-price-based.png" alt="POS with non-price-based product selected: Total Price button disabled" class="img-fluid" style="max-width: 100%;"/>
    </p>
    <p class="text-muted">
        <em>For a product that does <strong>not</strong> have "Price-based in POS" enabled (e.g. Bagel), the Total Price button stays disabled. You cannot sell it by the customer's requested total price - only by quantity and unit price.</em>
    </p>

    <h2>Edge cases</h2>
    <p>No order line selected, product without the flag, zero price, or invalid input are handled with clear alert messages; the button is disabled when not applicable.</p>
    <p>
        <img src="pos-empty-order-total-price-button-disabled.png" alt="POS screen with no products in order: Total Price button visible but disabled" class="img-fluid" style="max-width: 100%;"/>
    </p>
    <p class="text-muted"><em>POS with no products in the order: the Total Price button is visible but disabled (cannot be clicked) until a price-based product line is selected.</em></p>
</div>
    """,
    'category': "Point of Sale",
    'icon': '/pos_total_price_button/static/description/icon.png',
    'images': ['static/description/cover.png'],
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
    'price': 37,
    'currency': 'USD',
}
