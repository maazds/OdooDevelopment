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
    StudentAge = fields.Char('Age')

    orm_methods = fields.Char('orm')
    def get_name_copy(self):
        for i in self:
            return self.StudentDOB

    # Get all the records
    @api.onchange('orm_methods')
    def get_all_rec(self):
        for rec in self:
            # all records
            partner_data = self.env['res.partner'].search([])
            print('All Partners : ' , partner_data)
            # by field name match
            partner_data = self.env['res.partner'].search([('name','=','Azure Interior')])
            print('record by field value match : ', partner_data.name)
            """In Odoo, the read() method is used to retrieve data from records in a specified model. It returns a list of dictionaries, where each dictionary represents the data of a single record. Here's how you can use the read() method:"""
            # read all the data
            partner_data = self.env['res.partner'].search([]).read()
            print('Read',partner_data)
    #         limiting fields
            partner_data = self.env['res.partner'].search([]).read(['name','id'])
            print('Read', partner_data)
    #         write the existing field name to new name
            self.env['res.partner'].search([('name','=','Azure Interior')]).write({'name':'Maaz'})
    #         create a new record
            self.env['res.partner'].create({'name':'ali'})
    #         delete
            self.env['res.partner'].search([('name','=','ali')]).unlink()
            # search count on all rec
            x = self.env['res.partner'].search_count([])
            print(x)
    #         search count on the basis of fields ==== case sensitive
            x = self.env['res.partner'].search_count([('name','=','Maaz')])
            print(x)
            """In Odoo, the copy() method is used to duplicate existing records. It creates a new record with the same field values as the original record, optionally allowing you to specify new values for certain fields. Here's how you can use the copy() method:"""
            self.env['res.partner'].browse(10).copy({'phone':'03498223349'})
    #         field get
            """Retrieve metadata information about fields of a model"""
            field_info = self.env['res.partner'].fields_get()
            # print(field_info)
            for name, info in field_info.items():
                print('name',name)
                print('info',info.get('type',''))
                print('info',info.get('string',''))
            """default_get() is commonly used when you want to pre-fill fields with default values when creating new records. It allows you to define default values for fields dynamically based on certain conditions."""
            default_get_fields =self.env['res.partner'].default_get(['name'])
            print(default_get_fields)
    #         call
            """This will invoke the compute_subtotal() method on the sale.order.line model for the specific sales order line record identified by order_line_id."""
            record_data = self.env['odoo.fields'].browse(1)
            print(record_data.get_name_copy())
    def default_get(self,fields_list):
        defaults = super(OdooFields,self).default_get(fields_list)
        if 'StudentAge' in fields_list:
            defaults['StudentAge'] = self.env.user.partner_id.name
        return defaults
    # @api.onchange('StudentDOB')
    # def _student_age(self):
    #     pass
    #     # today = date.today()
    #     # x = fields.Date.today()
    #     # #THis is a testing brnach



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
