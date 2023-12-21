# -*- coding: utf-8 -*-
{
    'name': "task_manager",

    'summary': "Odoo 17",

    'description': """
        Task Manager For Odoo 17
    """,

    'author': "Arsalan +923158375182",
    'website': "https://www.yourcompany.com",


    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base_setup','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

