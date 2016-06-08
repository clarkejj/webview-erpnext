import frappe


def get_context(context):
	#context.planned_foobars = get_foobars("Planned")

	# show only 20 past foobars
	#context.past_foobars = get_foobars("Completed", limit_page_length=20)
	context.foobars = get_foobars(limit_page_length=20)

def get_foobars(**kwargs):
	return frappe.get_all("Foobar",
		fields=["foobarid", "foobardesc", "foobardate", "page_name", "parent_website_route"], **kwargs)


def get_list_context(context):
	context.title = _("Foobars")
	context.introduction = _('Current Foobars')

