# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class helpdesk_task(models.Model):

    _inherit = 'helpdesk.ticket'

    date_final = fields.Date( string="Fecha Limite")
    limit = fields.Char(compute='_calculate_days', readonly=True, store=False)
    limit_store = fields.Char(string="Fecha limite Calculada")


    @api.multi
    def _calculate_days(self):
        for l in self:
            if l.date_final:
                format_str = '%Y-%m-%d'
                current = datetime.datetime.now().date()
                limit = datetime.datetime.strptime(l.date_final, format_str).date()
                days_range = "%d Días restantes"  % (abs(limit - current).days)
                if current < limit:
                    self.limit = days_range
                    self.env.cr.execute("UPDATE helpdesk_ticket set limit_store = '%s' WHERE id = %d" % (days_range, l.id))
                if current == limit:
                    self.limit = 'Para terminar hoy'
                    self.env.cr.execute("UPDATE helpdesk_ticket set limit_store = '%s' WHERE id = %d" % ('Para terminar hoy', l.id))
                if current > limit:
                    self.limit = 'Vencido'
                    self.env.cr.execute("UPDATE helpdesk_ticket set limit_store = '%s' WHERE id = %d" % ('Vencido', l.id))
