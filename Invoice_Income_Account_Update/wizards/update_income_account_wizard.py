from odoo import models, fields, api

class AccountMoveUpdateIncomeAccountWizard(models.TransientModel):
    _name = 'account.move.update.income.account.wizard'
    _description = 'Update Income Account Wizard'

    move_id = fields.Many2one('account.move', string='Invoice', required=True)
    income_account_id = fields.Many2one('account.account', 
        string='Income Account', 
        required=True,
        domain="[('account_type', 'in', ['income_other', 'income']),('company_id', '=', company_id)]"
    )
    company_id = fields.Many2one('res.company', related='move_id.company_id')

    def action_update_income_account(self):
        self.ensure_one()
        for line in self.move_id.invoice_line_ids:
            line.account_id = self.income_account_id
        return {'type': 'ir.actions.act_window_close'}