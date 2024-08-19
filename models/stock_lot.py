from odoo import models, fields, api

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    ancho = fields.Float(string="Ancho", required=True)
    gramaje = fields.Float(string="Gramaje", required=True)
    tipo = fields.Char(string="Tipo", required=True)
    kilos = fields.Float(string="Kilos", required=True)
    planta = fields.Char(string="Planta", required=True)
    folio = fields.Char(string="Folio", required=True)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        # Aquí puedes agregar lógica para autocompletar algunos campos personalizados en función del producto
        if self.product_id:
            # Ejemplo de lógica para autocompletar o calcular valores
            self.tipo = self.product_id.default_code  # Solo un ejemplo simple
