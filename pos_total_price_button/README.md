# POS Price-based Products

## Requirements

- **Odoo 19** (Community or Enterprise)
- **Point of Sale** app installed and used in your database

---

## Overview

This Odoo 19 module adds a **Total Price** button to the Point of Sale control-buttons area.  
When the cashier clicks **Total Price**, the numpad switches to Total Price mode (the button is highlighted as active). The cashier types the desired total amount using the numpad and the system automatically computes and updates the correct quantity in real time (Qty = Total ÷ Unit Price).

The button is only **enabled** when the currently selected order line belongs to a product that has the **"Price-based in POS"** flag turned on (`pos_price_based = True`).  
For all other products the button is rendered in a disabled state and cannot be clicked.

---

## Features

| # | Feature | Detail |
|---|---------|--------|
| 1 | **Total Price button in POS** | Injected before the *More* button in the ControlButtons area |
| 2 | **Per-product access control** | Button is disabled unless the selected product has `pos_price_based = True` |
| 3 | **Numpad Total Price mode** | Clicking the button activates Total Price mode (button highlighted); numpad input updates Qty = Total ÷ Unit Price in real time |
| 4 | **Edge-case handling** | Zero unit price, no order, no selected line — button is disabled; invalid/zero numpad values are ignored gracefully |

---

## How It Works

1. In the product form, open the **Point of Sale** tab. The **"Price-based in POS"** checkbox is located directly below the **"Is a Weighed Product?"** (`to_weight`) field. Enable it.

2. In the POS session, add that product to the order and select its order line.

3. The **Total Price** button in the control-buttons area becomes clickable.

4. Click **Total Price**. The button turns active (highlighted) and the numpad switches to **Total Price mode**.

5. Type the desired total amount using the numpad (e.g. `2`). The system computes:
   ```
   Qty = EnteredTotal / UnitPrice
   ```
   **Example:** UnitPrice = 8 JOD/kg, EnteredTotal = 2 → Qty = 0.25

6. The order line quantity is updated to the computed value in real time. The unit price and line total reflect the entered amount.

---

## Product Configuration

The `pos_price_based` Boolean field is added to `product.template`.

| Field | Model | Default |
|-------|-------|---------|
| `pos_price_based` | `product.template` | `False` |

It is exposed in the product form under the **Point of Sale** tab, immediately after the **"Is a Weighed Product?"** (`to_weight`) field.  
It is also loaded into the POS client automatically so that the button state is reactive without extra RPC calls.

---

## Installation

1. Place the `pos_total_price_button` folder inside your Odoo addons path.
2. Update the app list and install the module **POS Price-based Products**.

For detailed steps (e.g. development setup, upgrading), see [INSTALL.md](INSTALL.md).

---

## Edge Cases

| Situation | Behaviour |
|-----------|-----------|
| No order line selected | Button is disabled; clicking has no effect |
| Product has `pos_price_based = False` | Button is disabled; clicking has no effect |
| No active order | Button is disabled |
| Unit price is 0 or negative | Button is disabled (cannot divide by zero or negative price) |
| Entered total is 0 or negative / non-numeric | Quantity is not changed; invalid numpad input is ignored |

**Example (valid case):**  
Product "Tomatoes" has unit price **10 JOD/kg** and **Price-based in POS** enabled. You add 1 kg to the order, select the line, then click **Total Price** (button turns active) and type **25** on the numpad.  
→ Qty becomes **2.5** kg, line total = **25.00 JOD**.

**Example (zero or negative input):**  
Same product, you click **Total Price** and type **0** or a non-numeric value.  
→ The quantity is not changed; the numpad input is ignored.

---

## Test Checklist

- [ ] Enable `pos_price_based` on a product (e.g. price 8 JOD/kg)
- [ ] Open POS and add the product to the order
- [ ] Select the order line — verify **Total Price** button is **enabled**
- [ ] Click **Total Price** — verify button turns **active** (highlighted) and numpad is in Total Price mode
- [ ] Type `2` on the numpad — confirm Qty = 0.25 and line total = 2.00
- [ ] Deselect the line (no line selected) — verify button is **disabled**
- [ ] Add a product without `pos_price_based` — verify button is **disabled**
- [ ] With a flagged product, activate Total Price mode and type `0` — expect quantity unchanged

---

## Module Structure

```
pos_total_price_button/
├── __manifest__.py                        # Module metadata
├── __init__.py
├── models/
│   ├── product_template.py               # Adds pos_price_based field to product.template
│   └── pos_product.py                    # Loads pos_price_based into POS client data
├── views/
│   └── product_template_view.xml         # Adds "Point of Sale" tab on product form
└── static/src/
    ├── js/
    │   └── pos_total_price_button.js     # Patches ControlButtons + OrderSummary for Total Price numpad mode
    └── xml/
        └── pos_total_price_button.xml    # QWeb template: injects disabled-aware, active-state Total Price button
```

---

## Troubleshooting

| Issue | What to check |
|-------|----------------|
| **Total Price button never enabled** | Ensure the product has **Price-based in POS** checked in the product form (Point of Sale tab), and that the order line for that product is selected. |
| **Button not visible in POS** | Clear browser cache, restart Odoo, and reload the POS session (close and reopen the POS interface). |
| **Button stays disabled despite valid product** | The product’s unit price may be 0 or negative. Set a valid unit price on the product. |
| **Quantity not updating when typing** | Ensure the Total Price button is active (highlighted). Click it again to re-enter Total Price mode, then type the total on the numpad. |

---

## License

This module is distributed under the **LGPL-3** license (see `__manifest__.py`).
