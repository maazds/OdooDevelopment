from odoo import api, fields, models,_


class OdooFields(models.Model):
    _name = 'odoo.fields'
    _rec_name = 'name'
    _description = 'A Complete model of the fields in odoo'

    name = fields.Char(string='Name', required=True)
    form_no = fields.Char(string="Form No", required=True,copy=False,readonly=True,default=lambda self:_('New'))

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
