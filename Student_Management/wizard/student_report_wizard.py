from odoo import api,models,fields

class StudentReportWizard(models.TransientModel):
    _name = 'student.report.wizard'
    _description = 'Student Report Wizard'

    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    report_file = fields.Binary('Excel File',readonly=True,attachment=False)
    report_filename = fields.Char('FileName',readonly=True)


    def action_export_excel(self):
        return True