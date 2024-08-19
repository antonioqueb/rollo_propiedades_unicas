{
    'name': 'Propiedades Únicas de Rollo',
    'version': '1.0',
    'author': 'TuNombre',
    'category': 'Inventario',
    'summary': 'Gestión de propiedades únicas por rollo',
    'description': """
        Este módulo permite gestionar propiedades únicas de cada rollo (ancho, gramaje, tipo, kilos, planta, folio)
        durante la recepción de productos y genera etiquetas personalizadas.
    """,
    'depends': ['stock', 'base'],
    'data': [
        'views/stock_picking_views.xml',
        'views/stock_lot_views.xml',
        'views/assets.xml',
        'report/rollo_label_template.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
stock_picking_views.xml