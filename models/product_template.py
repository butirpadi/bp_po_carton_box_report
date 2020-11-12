from odoo import models, fields, api, _
from odoo.exceptions import UserError


class WarnaBox(models.Model):
    _name = 'warna.box'

    name = fields.Char(string='Name', required=True, )


class JenisCarton(models.Model):
    _name = 'jenis.carton'

    name = fields.Char(string='Name', required=True, )


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    warna_box_id = fields.Many2one('warna.box', string='Warna')
    jenis_carton_id = fields.Many2one('jenis.carton', string='Jenis Carton')
    isi_per_box = fields.Integer(string='Isi per Box', default=None)
    is_carton_box = fields.Boolean(string='Karton Box', default=False)

    @api.onchange('length', 'width', 'height')
    def _auto_calculate_volume(self):
        if self.length and self.width and self.height:
            self.volume = float(self.length) * float(self.width) * float(self.height)
