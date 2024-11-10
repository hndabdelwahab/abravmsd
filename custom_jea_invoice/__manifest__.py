{
    'name': 'JEA Custom Invoice Template',
    'version': '17.0.0.0',
    'category': 'Accounting',
    'summary': '',
    'author': 'Hind',
    'depends': ['base','account' ],
    'data': [
        'views/invoice_temp.xml',
    ],
    
    'assets': {
        'web.report_assets_common': [
            '/custom_jea_invoice/static/**/*',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}