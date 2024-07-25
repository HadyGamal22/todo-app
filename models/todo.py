from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ModelA(models.Model):
    _name = 'todo.app'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description='To-Do'

    line_ids=fields.One2many('lines','task_id')
    name = fields.Char(required=True)
    description = fields.Text()
    active = fields.Boolean(default=True)
    date = fields.Date(tracking=1)
    estimated_time = fields.Date()
    state=fields.Selection([
        ('new','New'),
        ('progress', 'Progress'),
        ('complete', 'Complete'),
        ('closed', 'Closed'),
    ],default='new')

    _sql_constraints = [
        ('unique_name_must', 'unique("name")', 'This name must be unique')
    ]


    @api.onchange('name')
    def _onchange_price(self):
        for rec in self:
            print("inside the compute field")

            return {
                'warning':{
                    'title':'Your name must be good ',
                    'message':"cant do it with random shape",
                    'type':"notification"
                }
            }

    def action_new(self):
        for rec in self:
            rec.state = 'new'
    def action_closed(self):
        for rec in self:
            rec.state = 'closed'
    def action_progress(self):
        for rec in self:
            rec.state='progress'
    def action_complete(self):
        for rec in self:
            rec.state='complete'
    @api.model_create_multi
    def create(self,vals):
        res=super(ModelA,self).create(vals)
        # res=super(self).create(self,vals)
        print("inside the create method")
        print("self",self)
        print("vals",vals)
        return res
    @api.model
    def _search(self,domain,offset=0,limit=None,order=None,access_rights_uid=None):
        res = super(ModelA, self)._search(domain,offset=0,limit=None,order=None,access_rights_uid=None)
        # res=super(self).create(self,vals)
        print("inside the search method")
        print("self", self)
        print("domain", domain)
        return res

    def write(self,vals):
        res = super(ModelA, self).write(vals)
        # res=super(self).create(self,vals)
        print("inside the write method")
        print("self of the write", self)
        print("vals odf the write ", vals)
        return res

    def unlink(self):
        res = super(ModelA, self).unlink()
        # res=super(self).create(self,vals)
        print("inside the delete method")
        print("self of the write", self)
        # print("vals odf the write ", vals)
        return res



