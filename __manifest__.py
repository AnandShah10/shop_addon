# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'shop_addon',
    'version': '1.0',
    'summary': "shop addon module",
    'sequence': 10,
    'author': "anand",
    'description': """
My shop addon module
""",
    'category': 'Custom/Website_shop',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['mail', 'website','website_sale'],
    'data': [
        'views/shop.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
