# -*- coding: utf-8 -*-
from odoo import http

# class HelpdeskTask(http.Controller):
#     @http.route('/helpdesk_task/helpdesk_task/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/helpdesk_task/helpdesk_task/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('helpdesk_task.listing', {
#             'root': '/helpdesk_task/helpdesk_task',
#             'objects': http.request.env['helpdesk_task.helpdesk_task'].search([]),
#         })

#     @http.route('/helpdesk_task/helpdesk_task/objects/<model("helpdesk_task.helpdesk_task"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('helpdesk_task.object', {
#             'object': obj
#         })