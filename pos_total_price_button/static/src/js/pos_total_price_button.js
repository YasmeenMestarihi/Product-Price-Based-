/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(ControlButtons.prototype, {
    get isTotalPriceEnabled() {
        const order = this.currentOrder;
        if (!order) return false;
        const orderLine = order.getSelectedOrderline();
        if (!orderLine) return false;
        return orderLine.product_id?.pos_price_based === true;
    },
    onClickTotalPrice() {
        try {
            const order = this.currentOrder;
            if (!order) {
                this.dialog.add(AlertDialog, {
                    title: "Error",
                    body: "No order found.",
                });
                return;
            }

            const orderLine = order.getSelectedOrderline();
            if (!orderLine) {
                this.dialog.add(AlertDialog, {
                    title: "Error",
                    body: "Select a product first.",
                });
                return;
            }

            const unitPrice = orderLine.price_unit;
            if (!unitPrice || unitPrice <= 0) {
                this.dialog.add(AlertDialog, {
                    title: "Error",
                    body: "Invalid price.",
                });
                return;
            }

            const totalStr = prompt("Enter total price:");
            if (!totalStr) return;
            const total = parseFloat(totalStr);
            if (isNaN(total) || total <= 0) {
                this.dialog.add(AlertDialog, {
                    title: "Error",
                    body: "Enter valid amount.",
                });
                return;
            }

            const quantity = total / unitPrice;
            if (orderLine.setQuantity) {
                orderLine.setQuantity(quantity);
            } else {
                orderLine.quantity = quantity;
            }

            this.dialog.add(AlertDialog, {
                title: "Success",
                body: `Quantity: ${quantity.toFixed(2)}\nTotal: ${(quantity * unitPrice).toFixed(2)}`,
            });
        } catch (error) {
            console.error("Error:", error);
            this.dialog.add(AlertDialog, {
                title: "Error",
                body: `Error: ${error.message}`,
            });
        }
    },
});