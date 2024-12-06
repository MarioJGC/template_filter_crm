from odoo import models,api

class MailComposerInherit(models.TransientModel):
    _inherit = 'mail.composer.mixin'
    _description = 'Email composition wizard'
    
    @api.model
    def default_get(self, fields_list):
        result = super(MailComposerInherit, self).default_get(fields_list)
        
        active_model = self.env.context.get('active_model')
        active_id = self.env.context.get('active_id')

        if active_model == 'crm.lead':
            lead = self.env['crm.lead'].browse(active_id)
            type_pipeline = lead.type_pipeline_text

            # Modificar el dominio de la plantilla en función de 'type_pipeline_text'
            if type_pipeline == 'GOBIERNO':
                print("Ingreso Gobierno")
                domain = "[('model', '=', model), '|', ('user_id', '=', False), ('user_id', '=', uid), ('x_studio_tipo', '=', 'GOBIERNO')]"
            elif type_pipeline == 'PRIVADAS':
                print("Ingreso Privadas")
                domain = "[('model', '=', model), '|', ('user_id', '=', False), ('user_id', '=', uid), ('x_studio_tipo', '=', 'PRIVADAS')]"
            else:
                domain = "[('model', '=', model), '|', ('user_id', '=', False), ('user_id', '=', uid)]"  # Dominio predeterminado

            result['template_id'] = domain  # Esto establecerá el dominio para el campo template_id
         
        return result
