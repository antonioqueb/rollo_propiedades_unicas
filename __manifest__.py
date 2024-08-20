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
    "depends": ["stock", "base", "web"],  # Asegúrate de incluir "web" para cargar el módulo JS correctamente.
   "data": [
            "views/stock_lot_views.xml",  # Este archivo debe cargarse primero para que las acciones estén definidas
            "views/rollo_menu_views.xml",  # Ahora puedes cargar el menú que hace referencia a las acciones definidas anteriormente
            "views/stock_picking_views.xml",
            "security/ir.model.access.csv"  # Incluye este archivo si es necesario.
],

    "assets": {  # La nueva estructura de assets.
        "web.assets_backend": [
            "rollo_propiedades_unicas/static/src/js/rollo_properties.js",  # Asegúrate de que las rutas sean correctas.
            "rollo_propiedades_unicas/static/src/css/rollo_properties.css"
        ],
    },
    "images": ["static/description/icon.png"],  # Puedes agregar íconos si lo necesitas.
    "installable": True,
    "auto_install": False,
    "application": False
}
