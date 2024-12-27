{
    'name': 'Product Discount Feature',

    'version': '1.0',

    'summary': 'Display product discounted price',

    'category': 'Website',

    'author': 'Muhammad Jawaid Iqbal',

    'depends': ['base', 'website_sale', 'sale_management', 'stock'],

    'data': [
        'views/product_template.xml',
        'views/website_sale_product_template.xml',
        'views/website_sale_cart.xml',
    ],

    'installable': True,

    'application': True,

    'auto_install': False,
}