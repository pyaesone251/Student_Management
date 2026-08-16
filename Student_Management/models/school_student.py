from odoo import api,fields,models

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    student_name = fields.Char('Student Name')
    student_id = fields.Char('Student ID')
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
    ],string='Gender')
    date_of_birth = fields.Date('Date Of Birth')
    phone_number = fields.Char('Phone Number')
    email_address = fields.Char('Email Address')
    address = fields.Text('Address')
    active = fields.Boolean('Active',default=True)

    # Relation
    class_id = fields.Many2one('school.class',string='Class')
    subject_ids = fields.Many2many('school.subject',string='Subjects')