# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HotelRegister(models.Model):
    _name ='hotel.hotel_register'
    _description = 'Hotel'

    name = fields.Char(string='Descripcion')
    customer = fields.Char(string='Cliente')
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('p','Presencial'),('W','Whatsapp'),('T','Telefonico')],string='Tipo',requeried = True)
    done = fields.Boolean(string='Realizada',readonly=True)
