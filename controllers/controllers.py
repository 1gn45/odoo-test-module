# -*- coding: utf-8 -*-
# from odoo import http


# class Testas(http.Controller):
#     @http.route('/testas/testas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testas/testas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('testas.listing', {
#             'root': '/testas/testas',
#             'objects': http.request.env['testas.testas'].search([]),
#         })

#     @http.route('/testas/testas/objects/<model("testas.testas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testas.object', {
#             'object': obj
#         })
