import frappe

def get_context(context=None):
	if context is None:
		context = {}

	website_item_meta = frappe.get_meta("Website Item")
	if website_item_meta.get_field("show_in_website"):
		filters = {"show_in_website": 1}
	elif website_item_meta.get_field("published_in_website"):
		filters = {"published_in_website": 1}
	elif website_item_meta.get_field("published"):
		filters = {"published": 1}
	else:
		filters = {}    

	products = frappe.get_all(
		"Website Item",
		filters=filters,
		fields=["name", "web_item_name", "item_name", "website_image", "route", "short_description"],
		limit_page_length=10
	)
	context["products"] = products

	return context