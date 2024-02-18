# -*- coding: utf-8 -*-
{
    'name': "Odoo Development",
    'summary': """
      Development of odoo Custom Addons
      """,
    'description': """
        Basic Concepts of custom module develpment in odoo
    """,
    'author': "Maaz Aslam",
    'website': "https://pk.linkedin.com/in/maazaslamoo7",
    'category': 'Development',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu_items.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

