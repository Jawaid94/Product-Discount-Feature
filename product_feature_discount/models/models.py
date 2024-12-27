from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    discount_percentage = fields.Float('Discount (%)')
    discounted_price = fields.Float("Discounted Price", compute="_compute_discounted_price")

    @api.depends('discount_percentage')
    def _compute_discounted_price(self):
        """
        Compute the discounted price based on the discount percentage.
        If discount_percentage is 0, return the original price.
        """
        for product in self:
            if product.discount_percentage > 0:
                product.discounted_price = product.list_price * (1 - product.discount_percentage / 100)
            else:
                product.discounted_price = product.list_price


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _prepare_order_line_values(
            self, product_id, quantity, linked_line_id=False,
            no_variant_attribute_values=None, product_custom_attribute_values=None,
            **kwargs
    ):
        # Added discount to sale order when creating sale order line
        values = super()._prepare_order_line_values(product_id, quantity, **kwargs)
        product = self.env['product.product'].browse(product_id)
        values.update({
            'discount': product.discount_percentage
        })
        return values


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_amt = fields.Float(compute='_compute_discount_amt')

    @api.depends('discount', 'price_unit')
    def _compute_discount_amt(self):
        # Computed discount amount
        for record in self:
            record.discount_amt = (
                    record.price_unit - record.price_unit * (1 - record.discount / 100)) if record.discount else 0.0


class Website(models.Model):
    _inherit = 'website'

    def sale_get_order(self, force_create=False, update_pricelist=False):
        # after recompute price function run the discount will be zero that will effect the calculation
        # so we update the discount on sale order line
        sale_order = super().sale_get_order(force_create=force_create, update_pricelist=update_pricelist)
        if update_pricelist:
            for sol in sale_order.order_line:
                sol.discount = sol.product_id.discount_percentage
        return sale_order