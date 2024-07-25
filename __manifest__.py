{
    'name': 'ToDo',
    'description': 'To-Do task that i take it from the vidos on playlist on youtube  ',
    'author': 'Hady Gamal',
    'depends': ['base','crm','sale_management','account_accountant','mail','contacts'],
    'data':[
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo.xml',
        'reports/property_report.xml',
    ],
    'assets': {
        'web.assets_backend':[
            'practice/static/src/css/property.css'
        ]
    }
    #F:\odoo\assuit_2023\hms\security
}
