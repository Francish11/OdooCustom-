# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class proyecto(models.Model):
#     _name = 'proyecto.proyecto'
#     _description = 'proyecto.proyecto'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api

class departamento (models.model):
    _name = "proyectos.departamento"
    _descripcion ="Define los atributos de un departamento"
    
    #Atributos
    nombreDpto = fields.char(string="nombre departamento", required=True)
    
class empleado(models.model):
    _name = "proyecto.empleado" 
    _descripcion = "Define los atributos de un empleado"
    
    #Atributos
    dniempleado = fields.char(string="DNI", Required=True)
    nombreEmpleado = fields.char(string= "nombre y apellido", required=True)
    fechaNacimiento = fields.Date(string= "Fecha Nacimiento", required=True, default = fields.date.today())
    direccionEmpleado = fields.char(string= "Direccion")
    telefonoEmpleado = fields.char(string= "Telefono")
    
class Proyecto(models.model):
    _name = "proyectos.proyecto"
    _descripcion = "Define los atributos del proyecto"
    
    #Atributos
    nombreProyecto = fields.char(string= "Nombre del Proyecto", required=True)
    tipoProyecto = fields.Selection(
        string= "Tipo de Proyecto", 
        selection = [('f' , 'Front-End'),('b','Back-End')],
        help="Tipo de Proyecto al que se esta destinando ")

    