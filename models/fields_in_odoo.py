from odoo import api, fields, models,_
from datetime import date

class OdooFields(models.Model):
    _name = 'odoo.fields'
    _rec_name = 'StudentName'
    _description = 'A Complete model of the fields in odoo'

    StudentName = fields.Char(string='Student Name', required=True)
    StudentFormNo = fields.Char(string="Form No", required=True,copy=False,readonly=True,default=lambda self:_('New'))
    StudentRegdNo = fields.Char(string="Registration No.")
    StudentDOB = fields.Date('Date of Birth')
    StudentAge = fields.Char('Age',compute ='_student_age')


    @api.onchange('StudentDOB')
    def _student_age(self):
        today = date.today()
    #     THis is a testing brnach



    # b_date = fields.Date(string='DOB', related='name_id.dob')
    # age = fields.Integer(string="Age", compute='_compute_age')
    # father_name = fields.Char(string="Father's Name")
    # mother_name = fields.Char(string="Mother's Name")
    # mobile = fields.Char(string='Mobile', related='name_id.mobile')
    # phone = fields.Char(string='Phone', related='name_id.phone')
    # gender = fields.Selection([
    #     ('other', 'Other'),
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    # ], srting='Gender', default='other')
    # blood_grp = fields.Selection([
    #     ('a+', 'A+'),
    #     ('b+', 'B+'),
    #     ('ab+', 'AB+'),
    #     ('ab-', 'AB-'),
    #     ('o+', 'O+'),
    #     ('o-', 'O-'),
    # ], string="Blood Group")
    # nationality = fields.Many2one('res.country', string='Nationality')
    # # class_history_ids = fields.One2many('school.class.history', 'student_id', string='Class History')
