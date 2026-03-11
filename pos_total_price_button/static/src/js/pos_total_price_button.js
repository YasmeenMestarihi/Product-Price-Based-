/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { OrderSummary } from "@point_of_sale/app/screens/product_screen/order_summary/order_summary";

patch(ControlButtons.prototype, {
    setup() {
        super.setup();
        this.numberBuffer = useService("number_buffer");
    },
    get isTotalPriceEnabled() {
        const order = this.currentOrder;
        if (!order) return false;
        const orderLine = order.getSelectedOrderline();
        if (!orderLine) return false;
        return orderLine.product_id?.pos_price_based === true;
    },
    get isTotalPriceMode() {
        return this.pos.numpadMode === "totalPrice";
    },
    onClickTotalPrice() {
        this.numberBuffer.capture();
        this.numberBuffer.reset();
        this.pos.numpadMode = "totalPrice";
    },
});

patch(OrderSummary.prototype, {
    _setValue(val) {
        if (this.pos.numpadMode === "totalPrice") {
            // "remove" is sent when the buffer is cleared (e.g. line deletion); skip in this mode
            if (val === "remove") {
                return;
            }
            const selectedLine = this.currentOrder.getSelectedOrderline();
            if (selectedLine) {
                const unitPrice = selectedLine.price_unit;
                if (unitPrice && unitPrice > 0) {
                    const total = parseFloat(val);
                    if (!isNaN(total) && total >= 0) {
                        selectedLine.setQuantity(total / unitPrice);
                    }
                }
            }
            return;
        }
        super._setValue(val);
    },
});