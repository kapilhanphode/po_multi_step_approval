# po_multi_step_approval

**Purchase Order – Multi-Step Approval Workflow
**
This module implements a custom multi-step approval process for Purchase Orders based on the total amount.

Approval Flow
**Department Manager Approval
**Required when PO amount exceeds **50,000**
PO cannot be confirmed without this approval

**CFO Approval
**Required when PO amount exceeds **100,000**
Confirmation is blocked until CFO approval is completed

**Legal Approval
**Triggered automatically when PO amount exceeds **200,000**
PO moves to a custom status “Under Legal Review”
Only users from the Legal Department group can approve
After legal approval, the PO proceeds to confirmation
Custom warning messages are shown if a user attempts to confirm a PO without the required approvals.

**Outstanding Vendor Bill Validation
**While creating a Purchase Order, the system checks for:
Any posted vendor bills
That are unpaid
With a due date within the last 90 days or earlier
If such bills exist, PO creation is blocked with a custom validation error message.
This validation ensures better vendor payment discipline and financial control.
