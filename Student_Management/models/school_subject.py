from odoo import api,fields,models

class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'School Subject'

    name = fields.Char('Subject Name')
    code = fields.Char('Subject Code')
    teacher_id = fields.Many2one('school.teacher',string='Teachers')
    description = fields.Text('Description')

    
