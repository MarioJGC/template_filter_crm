from odoo import models, fields, api

class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    type_pipeline_text = fields.Char(compute='_compute_calculate_team')

    @api.depends('team_id')
    def _compute_calculate_team(self):
        for record in self:
            if record.team_id and record.team_id.name == 'Public Pipeline Team':
                record.type_pipeline_text = 'GOBIERNO'
            else:
                record.type_pipeline_text = 'PRIVADAS'

