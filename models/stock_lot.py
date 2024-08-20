from odoo import models, fields, api

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    ancho = fields.Float(string="Ancho", required=True)
    gramaje = fields.Float(string="Gramaje", required=True)
    tipo = fields.Char(string="Tipo", required=True)
    kilos = fields.Float(string="Kilos", required=True)
    planta = fields.Char(string="Planta", required=True)
