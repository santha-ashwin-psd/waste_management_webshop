from . import __version__ as _version

app_name = "webshop_waste"
app_title = "webshop_waste"
app_publisher = "Frappe Technologies Pvt. Ltd."
app_description = "Open Source eCommerce Platform"
app_email = "contact@frappe.io"
app_license = "GNU General Public License (v3)"
app_version = _version

required_apps = ["payments", "erpnext"]

web_include_css = "webshop-web.bundle.css"

web_include_js = "web.bundle.js"

after_install = "webshop_waste.setup.install.after_install"
on_logout = "webshop_waste.webshop_waste.shopping_cart.utils.clear_cart_count"
on_session_creation = [
    "webshop_waste.webshop_waste.utils.portal.update_debtors_account",
    "webshop_waste.webshop_waste.shopping_cart.utils.set_cart_count",
]
update_website_context = [
    "webshop_waste.webshop_waste.shopping_cart.utils.update_website_context",
]

website_generators = ["Website Item", "Item Group"]

override_doctype_class = {
    "Payment Request": "webshop_waste.webshop_waste.doctype.override_doctype.payment_request.PaymentRequest",
    "Item Group": "webshop_waste.webshop_waste.doctype.override_doctype.item_group.webshop_wasteItemGroup",
    "Item": "webshop_waste.webshop_waste.doctype.override_doctype.item.webshop_wasteItem",
}

doctype_js = {
    "Item": "public/js/override/item.js",
    "Homepage": "public/js/override/homepage.js",
}

doc_events = {
    "Item": {
        "on_update": [
            "webshop_waste.webshop_waste.crud_events.item.update_website_item.execute",
            "webshop_waste.webshop_waste.crud_events.item.invalidate_item_variants_cache.execute",
        ],
        "before_rename": [
            "webshop_waste.webshop_waste.crud_events.item.validate_duplicate_website_item.execute",
        ],
        "after_rename": [
            "webshop_waste.webshop_waste.crud_events.item.invalidate_item_variants_cache.execute",
        ],
    },
    "Sales Taxes and Charges Template": {
        "on_update": [
            "webshop_waste.webshop_waste.doctype.webshop_settings.webshop_settings.validate_cart_settings",
        ],
    },
    "Quotation": {
        "validate": [
            "webshop_waste.webshop_waste.crud_events.quotation.validate_shopping_cart_items.execute",
        ],
    },
    "Price List": {
        "validate": [
            "webshop_waste.webshop_waste.crud_events.price_list.check_impact_on_cart.execute"
        ],
    },
    "Tax Rule": {
        "validate": [
            "webshop_waste.webshop_waste.crud_events.tax_rule.validate_use_for_cart.execute",
        ],
    },
}

has_website_permission = {
    "Website Item": "webshop_waste.webshop_waste.doctype.website_item.website_item.has_website_permission_for_website_item",
    "Item Group": "webshop_waste.webshop_waste.doctype.website_item.website_item.has_website_permission_for_item_group"
}

template_overrides = {
    "erpnext/templates/includes/transaction_row.html": "webshop_waste/templates/includes/transaction_row.html"
}

