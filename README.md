# po_multi_step_approval

**Purchase Order – Multi-Step Approval Workflow**

This module implements a custom multi-step approval process for Purchase Orders based on the total amount.

**Approval Flow**

**Department Manager Approval**
Required when PO amount exceeds **50,000**</br>
PO cannot be confirmed without this approval

**CFO Approval**
Required when PO amount exceeds **100,000**</br>
Confirmation is blocked until CFO approval is completed

**Legal Approval**</br>
Triggered automatically when PO amount exceeds **200,000**</br>
PO moves to a custom status “**Under Legal Review**”</br>
Only users from the Legal Department group can approve</br>
After legal approval, the PO proceeds to confirmation</br>
Custom warning messages are shown if a user attempts to confirm a PO without the required approvals.</br>

**Outstanding Vendor Bill Validation**</br>
While creating a Purchase Order, the system checks for:</br>
Any posted vendor bills</br>
That are unpaid</br>
With a due date within the last 90 days or earlier</br>
If such bills exist, PO creation is blocked with a custom validation error message.</br>
This validation ensures better vendor payment discipline and financial control.
