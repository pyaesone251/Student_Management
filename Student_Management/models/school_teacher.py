from odoo import api,fields,models

class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'School Teacher'

    name = fields.Char('Teacher Name')
    employee_id = fields.Char('Employee ID')
    phone = fields.Char('Phone')
    email = fields.Char('Email')
    date_joined = fields.Date('Join Date')
    active = fields.Boolean('Active',default='True')

    # relation
    subject_id = fields.Many2many('school.subject',string='Subjects')