# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Manufacturing Custom hasmicro',
    'version': '2.0',
    'category': 'Manufacturing/Manufacturing',
    'sequence': 55,
    'summary': 'Manufacturing Custom',
    'depends': ['mrp', 'mrp_account'],
    'description': "",
    'data': [
        # 'security/mrp_security.xml',
        # 'security/ir.model.access.csv',
        'views/mrp_bom_views.xml',
    ],
    'qweb': [],
    'demo': [
    
    ],
    'test': [],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
