# -*- coding: utf-8 -*-

{
    # Module Info
    "name": "Purchase Multi Step Approval",
    "version": "18.0.1.0.0",
    "category": "purchase",
    "summary": "Purcahse approval workflow and vendor outstanding bills",
    "description": """ 
    Purcahse approval workflow and vendor outstanding bills
    """,

    # Author
    "author": "Kapil",

    # Dependencies
    "depends": ["purchase", "account"],

    # Data File
    "data": [
        "security/purchase_security.xml",
        "views/purchase_order_view.xml",
    ],

    # Technical Info
    "installable": True,
    "application": False,
}
