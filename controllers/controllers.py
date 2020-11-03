# -*- coding: utf-8 -*-
from odoo import http

# class BpPoCartonBoxReport(http.Controller):
#     @http.route('/bp_po_carton_box_report/bp_po_carton_box_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bp_po_carton_box_report/bp_po_carton_box_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bp_po_carton_box_report.listing', {
#             'root': '/bp_po_carton_box_report/bp_po_carton_box_report',
#             'objects': http.request.env['bp_po_carton_box_report.bp_po_carton_box_report'].search([]),
#         })

#     @http.route('/bp_po_carton_box_report/bp_po_carton_box_report/objects/<model("bp_po_carton_box_report.bp_po_carton_box_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bp_po_carton_box_report.object', {
#             'object': obj
#         })