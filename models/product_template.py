from odoo import models, fields, api, _
from odoo.exceptions import UserError
from pprint import pprint


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

    volume = fields.Float('Volume', compute='_compute_volume', inverse='_set_volume',
                          help="The volume in m3.", store=True, digits=(16, 4))

    # replace from module wk_product_dimensions
    length = fields.Float(string='Length',)
    width = fields.Float(string='Width',)
    height = fields.Float(string='Height',)

    # temp for upgrade module
    temp_length = fields.Float(string='Length',)
    temp_width = fields.Float(string='Width',)
    temp_height = fields.Float(string='Height',)

    # @api.onchange('length', 'width', 'height')
    # def _auto_calculate_volume(self):
    #     factor = self.dimensions_uom_id.factor
    #     if self.dimensions_uom_id.uom_type == 'smaller':
    #         factor = 1/factor
    #     l = factor * self.length
    #     w = factor * self.width
    #     h = factor * self.height
    #     self.update({
    #         'volume': l * w * h
    #     })

    @api.multi
    def write(self, values):
        pprint(values)
        if 'length' in values or 'width' in values or 'height' in values:
            factor = self.dimensions_uom_id.factor
            print('factor : ' + str(factor))
            if self.dimensions_uom_id.uom_type == 'smaller':
                factor = 1/factor
            print('factor 2 : ' + str(factor))
            l = factor * (values['length']
                          if 'length' in values else self.length)
            w = factor * (values['width'] if 'width' in values else self.width)
            h = factor * (values['height']
                          if 'height' in values else self.height)
            print('L : ' + str(l))
            print('W : ' + str(w))
            print('H : ' + str(h))
            values['volume'] = l*w*h
            print('Vol : ' + str(l*w*h))

        # CODE HERE
        return super(ProductTemplate, self).write(values)
