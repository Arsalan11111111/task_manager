# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Odoo Module (task_manager):
# a. Create a new Odoo module named `task_manager`.
# b. Define a model named `Task` with fields: Title, Description, Deadline, and
# Completed.
# c. Create a menu item for the Task Management module.
# d. Implement basic CRUD operations for tasks.
# e. Add a Kanban view to display tasks.

class task_manager(models.Model):
    _name = 'task_manager.task_manager'
    _inherit = ['mail.thread',
                'mail.activity.mixin',
               ]
    _description = 'task_manager.task_manager'

    name = fields.Char("Title")
    description = fields.Text("Description")
    deadline = fields.Datetime("Deadline")
    stage = fields.Selection([('New','New'),('Completed','Completed')],default='New',string='Stage')
    stage_id = fields.Many2one(
        'task.manager.stage', string='Stage', index=True, tracking=True)

    days_to_dead_line = fields.Char("Days Left to Deadline",compute="_calculate_deadline")


    def _calculate_deadline(self):
        for rec in self:


            deadline = rec.deadline
                                                      # Replace 'record' with your Odoo record

            # Get the current date
            current_date = datetime.now()

            # Calculate the difference between the two dates
            date_difference = deadline.day - current_date.day

            if date_difference>0:

                rec.days_to_dead_line = date_difference
            else:
                rec.days_to_dead_line = "Deadline crossed"

            a= 1

    def action_complete(self):
        self.stage_id = self.env['task.manager.stage'].search([('name','=','Completed')]).id

class task_manager_stage(models.Model):
    _name = 'task.manager.stage'

    name = fields.Char("Name")
