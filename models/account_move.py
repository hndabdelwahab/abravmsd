from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_update_income_account(self):
        """Open wizard to update income account for all invoice lines"""
        return {
            'name': 'Update Income Account',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move.update.income.account.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
             'default_move_id': self.id,
            }
        }

