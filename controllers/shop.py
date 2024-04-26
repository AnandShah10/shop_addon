from odoo import http
from odoo.http import content_disposition, Controller, request, route
from odoo.addons.website_sale.controllers.main import WebsiteSale, Website
from markupsafe import Markup
import re


class SearchRecommendation(Website):
    @http.route()
    def autocomplete(self, search_type=None, term=None, order=None, limit=5, max_nb_chars=999, options=None):
        """
                Used To Show product_name field instead of name field in search recommendation.
        """
        print(options, term, search_type)
        res = super(SearchRecommendation, self).autocomplete(search_type=search_type, term=term, order=order,
                                                             limit=limit, max_nb_chars=max_nb_chars, options=options)
        print(res)
        print(http.request.httprequest.referrer, '??????????', http.request.httprequest.url)
        if 'shop' in str(http.request.httprequest.referrer):  # To only allow recommendation in shop
            products = request.env['product.template'].search([
                ('product_name', 'ilike', '%' + term + '%')
            ])
            for i in res['results']:
                for j in products:
                    ############################# Commented Code ##############################################
                    # print(j.name, '_______________________name......', j.product_name)
                    # searched_value = re.findall('<span class="text-primary">[^>]*</span>', str(i['name']),
                    #                             re.IGNORECASE)
                    # if searched_value:
                    #     searched_value = str(searched_value[0])
                    # else:
                    #     searched_value = ''
                    # searched_filtered_value = re.sub('<[^>]*?>', '', searched_value).replace('</span>', '')
                    ###########################################################################################

                    # To find default name for the recommendation
                    search_value = str(re.sub('<[^>]*?>', '', str(i['name']))).strip('\n').strip(
                        ' ')
                    if search_value:
                        if search_value == j.name:  # To change name to product_name
                            # Used to get exact case highlight in display as in product_name
                            term = re.findall(re.escape(term), j.product_name, flags=re.IGNORECASE)
                            if term:
                                term = term[0]
                            else:
                                term = ''
                            # To Give highlight to searched term (case insensitive)
                            return_val = re.sub(f'{re.escape(term)}',
                                                f'<span class="text-primary">{term}</span>',
                                                j.product_name,
                                                flags=re.IGNORECASE)
                            # return_val = j.product_name.replace(term, f'<span class="text-primary">{term}</span>')
                            print(term, '----------', return_val)
                            i['name'] = Markup(return_val)  # Return value as markup
        return res
