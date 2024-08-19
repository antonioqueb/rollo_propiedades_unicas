{
    "name": "Propiedades Únicas de Rollo",
    "version": "1.0",
    "summary": "Gestión de propiedades únicas por rollo",
    "description": """
        Este módulo permite gestionar propiedades únicas de cada rollo (ancho, gramaje, tipo, kilos, planta, folio)
        durante la recepción de productos y genera etiquetas personalizadas.
    """,
    "category": "Inventory",
    "author": "Alphaqueb Consulting S.A.S.",
    "website": "https://gestpro.cloud",
    "license": "LGPL-3",
    "depends": ["stock", "base", "web"],  # Incluye 'web' en las dependencias para asegurar la carga del módulo
    "data": [
        "views/stock_picking_views.xml",
        "views/stock_lot_views.xml",
        "report/rollo_label_template.xml",
        "security/ir.model.access.csv"  # Incluye el archivo de acceso a modelos, si es necesario
    ],
    "assets": {  # Sección de assets para gestionar CSS y JS en las versiones modernas de Odoo
        "web.assets_backend": [
            "rollo_propiedades_unicas/static/src/js/rollo_properties.js",
            "rollo_propiedades_unicas/static/src/css/rollo_properties.css"
        ],
    },
    "images": ["static/description/icon.png"],  # Agrega un ícono si es necesario
    "installable": True,
    "auto_install": False,
    "application": False
}
