# -*- coding: utf-8 -*-
{
    'name': "Report PO Karton Box",

    'summary': """
        Report PO Khusus untuk pembelian Karton Box""",

    'description': """
        Report PO Khusus untuk pembelian Karton Box

        Author : butirpadi
        Phone :  082398371825
    """,

    'author': "butirpadi",
    'website': "https://www.github.com/butirpadi",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'purchase_order_report_mod', 'merge_delivery_btr_mod'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_view.xml',
        'reports/report.xml',
        'reports/purchase_order_box_carton_report.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
