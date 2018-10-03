# -*- coding: utf-8 -*-
from odoo import http

# class Inmoviliaria(http.Controller):
#     @http.route('/inmoviliaria/inmoviliaria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inmoviliaria/inmoviliaria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inmoviliaria.listing', {
#             'root': '/inmoviliaria/inmoviliaria',
#             'objects': http.request.env['inmoviliaria.inmoviliaria'].search([]),
#         })

#     @http.route('/inmoviliaria/inmoviliaria/objects/<model("inmoviliaria.inmoviliaria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inmoviliaria.object', {
#             'object': obj
#         })