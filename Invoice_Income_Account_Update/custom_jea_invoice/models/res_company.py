from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    company_stamp = fields.Binary(string='Company Stamp', attachment=True)
