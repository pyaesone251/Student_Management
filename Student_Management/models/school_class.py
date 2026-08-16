from odoo import api,fields,models

class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char('Class Name')
    code = fields.Char('Class Code')
    academic_year = fields.Char('Academic Year')
    description = fields.Text('Description')
    active = fields.Boolean('Active',default='True')
    