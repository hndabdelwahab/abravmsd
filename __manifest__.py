{
    'name': 'Invoice Income Account Update',
    'version': '17.0.0.0',
    'category': 'Accounting',
    'summary': 'Add button to update income account for all invoice lines',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/update_income_account_wizard.xml',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
}