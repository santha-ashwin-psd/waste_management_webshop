# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt
import unittest

import frappe

from webshop_waste.webshop_waste.doctype.webshop_waste_settings.webshop_waste_settings import (
	ShoppingCartSetupError,
)


class Testwebshop_wasteSettings(unittest.TestCase):
	def tearDown(self):
		frappe.db.rollback()

	def test_tax_rule_validation(self):
		frappe.db.sql("update `tabTax Rule` set use_for_shopping_cart = 0")
		frappe.db.commit()  # nosemgrep

		cart_settings = frappe.get_doc("webshop_waste Settings")
		cart_settings.enabled = 1
		if not frappe.db.get_value("Tax Rule", {"use_for_shopping_cart": 1}, "name"):
			self.assertRaises(ShoppingCartSetupError, cart_settings.validate_tax_rule)

		frappe.db.sql("update `tabTax Rule` set use_for_shopping_cart = 1")

	def test_invalid_filter_fields(self):
		"Check if Item fields are blocked in webshop_waste Settings filter fields."
		from frappe.custom.doctype.custom_field.custom_field import create_custom_field

		setup_webshop_waste_settings({"enable_field_filters": 1})

		create_custom_field(
			"Item",
			dict(owner="Administrator", fieldname="test_data", label="Test", fieldtype="Data"),
		)
		settings = frappe.get_doc("webshop_waste Settings")
		settings.append("filter_fields", {"fieldname": "test_data"})

		self.assertRaises(frappe.ValidationError, settings.save)


def setup_webshop_waste_settings(values_dict):
	"Accepts a dict of values that updates webshop_waste Settings."
	if not values_dict:
		return

	doc = frappe.get_doc("webshop_waste Settings", "webshop_waste Settings")
	doc.update(values_dict)
	doc.save()


test_dependencies = ["Tax Rule"]
