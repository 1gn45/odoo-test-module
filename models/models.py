# -*- coding: utf-8 -*-

from odoo import models, fields


class Car(models.Model):
    _name = "car.car"

    name = fields.Char(string='name')
    horse_power = fields.Integer(string="Horse Power")
    door_number = fields.Integer(string=" string Doors number")
    driver_id   = fields.Many2one("res.partner", string="Driver")
    parking_id  = fields.Many2one("parking.parking" "Parking id")

class Parking(models.Model):
    _name = "parking.parking"

    name = fields.Char(string='Name')
    car_ids = fields.One2many("car.car", "parking_id", string="Cars")

# class testas(models.Model):
#     _name = 'testas.testas'
#     _description = 'testas.testas'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
