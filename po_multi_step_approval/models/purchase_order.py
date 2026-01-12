from datetime import timedelta
from odoo import _, api, models, fields
from odoo.exceptions import UserError, ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    _description = "Purchase Order"

    state = fields.Selection(selection_add=[('under_legal_review', 'Under Legal Review'), ],
                             ondelete={'under_legal_review': 'cascade'})
    legal_approval = fields.Boolean(string="Legal Approval")
    department_manager_approval = fields.Boolean(string="Department Manager Approval")
    cfo_approval = fields.Boolean(string="CFO Approval")


    def check_approval(self):
        for order in self:
            if order.amount_total > 50000 and not order.department_manager_approval:
                raise UserError(_("Department Manager approval is required."))
            if order.amount_total > 100000 and not order.cfo_approval:
                raise UserError(_("CFO approval is required."))

    def button_confirm(self):
        for order in self:
            order.check_approval()
            if order.amount_total > 200000 and not order.legal_approval:
                order.state = 'under_legal_review'
                return True
        return super(PurchaseOrder, self).button_confirm()

    def action_department_manager_approval(self):
        for rec in self:
            rec.department_manager_approval = True

    def action_cfo_approval(self):
        for rec in self:
            rec.cfo_approval = True

    def action_legal_approval(self):
        for order in self:
            if order.state != 'under_legal_review':
                raise UserError(
                    _("Legal approval is only allowed when the PO is under Legal Review.")
                )
            order.legal_approval = True
            order.state = 'draft'
            return super(PurchaseOrder, self).button_confirm()

    @api.model_create_multi
    def create(self, vals_list):
        orders = super(PurchaseOrder, self).create(vals_list)

        for order in orders:
            today = fields.Date.today()
            last_90_days = today - timedelta(days=90)

            bills = self.env["account.move"].search([
                ("partner_id", "=", order.partner_id.id),
                ("move_type", "=", "in_invoice"),
                ("state", "=", "posted"),
                ("payment_state", "!=", "paid"),
                ("invoice_date_due", "<=", today),
                ("invoice_date_due", ">=", last_90_days),
            ], limit=1)

            if bills:
                raise ValidationError(
                    _(
                        "You cannot create a Purchase Order for this vendor.\n\n"
                        "The vendor has unpaid bills due today or within the last 90 days."
                    )
                )

        return orders
