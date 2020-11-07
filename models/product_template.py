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

    # is_carton_box = fields.Boolean(string='Carton/Box')
    warna_box_id = fields.Many2one('warna.box', string='Warna')
    jenis_carton_id = fields.Many2one('jenis.carton', string='Jenis Carton')
    # box_length = fields.Integer(string='Length', default=None)
    # box_width = fields.Integer(string='Width', default=None)
    # box_height = fields.Integer(string='Height', default=None)
    isi_per_box = fields.Integer(string='Isi per Box', default=None)
