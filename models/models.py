# -*- coding: utf-8 -*-

from odoo import models, fields, api
from openerp.exceptions import ValidationError


class Car(models.Model):
    _name = "car.car"

    name = fields.Char(string='name')
    horse_power = fields.Integer(string="Horse Power")
    door_number = fields.Integer(string=" string Doors number")

    driver_id = fields.Many2one("res.partner", string="Driver")
    parking_id = fields.Many2one("parking.parking", string="Parking")
    feature_ids = fields.Many2many("car.feature", string="Features")
    total_speed = fields.Integer(string="Total speed", compute="get_total_speed")

    status = fields.Selection([('new', 'New'), ('used', 'Used'), ('sold', 'Sold')], string='Status', default="new")

#### "create table" original funkcijos pakeitimas galima apdirbti inputus ir apdirbtus padeti i duombaze
####butinas dekoratorius ir butinas pavadinimas create nes jis pakeicia orginalia fnc
    @api.model
    def create(self, vals):
        print("----------CREATE FUNKCIJA---------------")
        vals['name']+=" papildomas tekstas reiksmeje i duombaze"
        if vals['horse_power']>10:
            raise ValidationError("The horse power can't be greater than 10")
        result=super(Car, self).create(vals)
        return result
#### Overwritinam funkcija write, (kai spaudziam edit.) butina write pavadinimas
    def write(self, vals):
        print("----------WRITE FUNKCIJA---------------")
        if vals['horse_power']>10:
            raise ValidationError("The horse power can't be greater than 10")
        result = super(Car, self).write(vals)
        return result
    ####Overwriting delete function
    def unlink(self):
        print("---------OVERWRITING DELETE FNC-----------")
        ##loopinam per pasirinktus istrinti elementus
        for a in self:
            if a.horse_power==8:
                raise ValidationError("Remove not possible with horse power=8")
        return super(Car, self).unlink(vals)



    def set_car_to_used(self):
        print('set_car_to_used')
        self.status='used'

    def set_car_to_sold(self):
        print('set_car_to_sold')
        self.status = 'sold'

    def get_total_speed(self):
        self.total_speed = self.horse_power * 50


class Parking(models.Model):
    _name = "parking.parking"

    name = fields.Char(string='Name')
    car_ids = fields.One2many("car.car", "parking_id", string="Cars")


class CarFeatures(models.Model):
    _name = "car.feature"

    name = fields.Char(string='Name')
    value = fields.Char(string='Value')

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
