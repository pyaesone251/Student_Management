from odoo import api,models,fields, _
from odoo.exceptions import ValidationError
import io
import xlsxwriter
import base64


class StudentReportWizard(models.TransientModel):
    _name = 'student.report.wizard'
    _description = 'Student Report Wizard'

    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    report_file = fields.Binary('Excel File',readonly=True,attachment=False)
    report_filename = fields.Char('FileName',readonly=True)


    def action_export_excel(self):
        self.ensure_one()
        if self.start_date > self.end_date:
            raise ValidationError(_("Start date can't be greater than end date "))

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output,{"in_memory":True})
        worksheet = workbook.add_worksheet("Student Report")

        title_format = workbook.add_format({
        "bg_color":"#0C97F4",
        "border":1,
        "bold":True,
        "font_size":16,
        "align":"center",
        })

        header_format = workbook.add_format({
            'border':1,
            'bold':True,
            'font_size':12,
            'align':'center',
        })
        text_format = workbook.add_format({
            "border":1,
            'align':'center',
        })
        date_format = workbook.add_format({
            "border":1,
            "num_format":"yyyy-mm-dd",
        })

        current_company = self.env.company
        worksheet.merge_range("A1:F1",current_company.name,title_format)
        worksheet.merge_range("A2:F2","Student List Report",title_format)

        students = self.env['school.student'].search([("date",">=",self.start_date),("date","<=",self.end_date)])

        worksheet.write(3,0,"No",header_format)
        worksheet.write(3,1,"Stutend ID",header_format)
        worksheet.write(3,2,"Student Name",header_format)
        worksheet.write(3,3,"Class Name",header_format)
        worksheet.write(3,4,"Phone",header_format)
        worksheet.write(3,5,"Email",header_format)

        worksheet.set_column("A:C",16)
        worksheet.set_column("D:F",22)

        row = 4
        for no,student in enumerate(students,start=1):
            worksheet.write(row,0,no,text_format)
            worksheet.write(row,1,student.sequence,text_format)
            worksheet.write(row,2,student.student_name,text_format)
            worksheet.write(row,3,student.class_id.name,text_format)
            worksheet.write(row,4,student.phone_number,text_format)
            worksheet.write(row,5,student.email_address,text_format)
            row+=1

        worksheet.write(row,0,f"Total Student : {len(students)}")

        workbook.close()
        filename = ("student_report"+str(self.start_date)+"_to_"+str(self.end_date))

        excel_data = output.getvalue()
        encode_excel = base64.b64encode(excel_data)
        self.report_file  = encode_excel
        self.report_filename = filename

        output.close()
        download_url = ("/web/content/"+self._name+"/"+str(self.id)+"/report_file/"+filename+"?download=true")
        return {
        "type":"ir.actions.act_url",
        "url":download_url,
        "target":"self",
        }