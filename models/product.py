from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
from odoo import http


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_name = fields.Char(string="Product Name")

    # @api.depends('name', 'default_code', 'product_name')
    # def _compute_display_name(self):
    #     """
    #             Changing display name as product_name
    #     """
    #     super(ProductTemplate, self)._compute_display_name()
    #     for i in self:
    #         if i.product_name:
    #             i.display_name = i.product_name

    @api.model
    def _search_get_detail(self, website, order, options):
        """
        To Include product_name field as search parameter in shop
        """
        print('hello finally search.................')
        search_details = super(ProductTemplate, self)._search_get_detail(website, order, options)
        if 'shop' in str(http.request.httprequest.referrer):  # To only able to use on shop
            search_details['search_fields'].append('product_name')
        return search_details
