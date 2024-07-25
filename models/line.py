from odoo import models, fields


class Lines(models.Model):
    _name = 'lines'

    name = fields.Char(required=True)
    description = fields.Text()
    hours = fields.Integer()

    task_id=fields.Many2one('todo.app')