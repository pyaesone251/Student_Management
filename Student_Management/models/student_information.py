from odoo import api,fields,models

class StudentInformation(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean('Is Student')
    student_code = fields.Char('Student Code')
    enrollment_date = fields.Date('Enrollment Date')