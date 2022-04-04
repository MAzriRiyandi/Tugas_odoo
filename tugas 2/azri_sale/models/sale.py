from odoo import _, api, fields, models
from odoo.exceptions import UserError


class SaleSale(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    create_auto = fields.Many2one(comodel_name='mrp.bom', string='BoM')
    auto_create = fields.Char(compute='_compute_auto_create', string='Bom')
    
    @api.depends('create_auto')
    def _compute_auto_create(self):
        for record in self:
            record.auto_create = self.env['mrp.bom'].search([('id','=',record.create_auto.id)]).mapped('product_tmpl_id').bom_line_ids
