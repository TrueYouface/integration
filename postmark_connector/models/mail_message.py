# Copyright 2022 Samet Altuntaş (https://github.com/samettal)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class MailMessage(models.Model):
    _inherit = "mail.message"
    _description = "Adds 'opened' state to mail.message through postmark integration"

    postmark_message_id = fields.Char(
        string="Postmark Message ID",
        help="This field shows Postmark's message_id",
        readonly=True,
    )
