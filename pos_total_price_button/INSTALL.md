# Installation and Setup — POS Price-based Products (Odoo 19)

## Prerequisites

- Odoo 19 installed and running.
- Administrator access to the Odoo backend.

## Installation Steps

1. **Download the Module**
   Clone or download this repository and locate the `pos_total_price_button` folder.

2. **Copy to Addons Directory**
   Place the `pos_total_price_button` folder inside your Odoo custom addons directory (the path configured in `addons_path` in your `odoo.conf`).

3. **Set Permissions** *(Linux/macOS)*
   ```bash
   sudo chown -R odoo:odoo pos_total_price_button
   sudo chmod -R 755 pos_total_price_button
   ```
   Alternatively, run the included helper script:
   ```bash
   bash pos_total_price_button/install.sh
   ```

4. **Update the App List**
   - Log in to Odoo as an administrator.
   - Navigate to **Apps** and click **Update Apps List**.

5. **Install the Module**
   - Search for **"POS Price-based Products"** in the Apps list.
   - Click **Install**.

6. **Restart Odoo** *(if required)*
   ```bash
   sudo systemctl restart odoo.service
   ```

---

## Enabling the Feature for a Product

1. Go to **Point of Sale → Products → Products** (or **Inventory → Products**).
2. Open the product you want to enable.
3. Click the **Point of Sale** tab.
4. Locate the **"Is a Weighed Product?"** field and check the **"Price-based in POS"** checkbox immediately below it.
5. Click **Save**.

> Only products with **"Price-based in POS"** enabled will allow cashiers to use the **Total Price** button in the POS interface.

---

## Using the Feature in the POS Session

1. Start a new POS session.
2. Add a product that has **"Price-based in POS"** enabled to the order.
3. Select the order line for that product.
4. Click the **Total Price** button in the control-buttons area (it is enabled only for flagged products).
5. Enter the desired total amount in the prompt (e.g. `10`).
6. The system calculates `Qty = Total ÷ Unit Price` and updates the order line quantity automatically.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Module not visible in Apps | Make sure you ran **Update Apps List** and that the folder is in the correct `addons_path` |
| **Total Price** button is greyed out | The selected product does not have **"Price-based in POS"** enabled — enable it in the product form |
| **Total Price** button does not appear at all | Confirm the module is installed and the POS assets were reloaded (restart the server or clear the browser cache) |
| "Invalid price." alert | The product's sale price is 0 — set a positive unit price before using this feature |
