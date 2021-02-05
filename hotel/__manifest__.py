# -*- coding: utf-8 -*-
{
    'name': "Hotel",

    'summary': """
        Manage and Administration your Hotel""",

    'description': """
        the purpurse of this app it to help a many people who need to manage your hotel.
    """,

    'author': "Normand Terceros",
    'website': "http://www.normandweb.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hotel_view.xml',
        #'views/templates.xml',
    ],
    'application': True,
}
