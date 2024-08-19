from odoo import models, fields

class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    ancho = fields.Float(string="Ancho")
    gramaje = fields.Float(string="Gramaje")
    tipo = fields.Char(string="Tipo")
    kilos = fields.Float(string="Kilos")
    planta = fields.Char(string="Planta")
    folio = fields.Char(string="Folio")
