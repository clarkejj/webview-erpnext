# -*- coding: utf-8 -*-
# Copyright (c) 2015, ABC and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator

class Foobar(WebsiteGenerator):
	website = frappe._dict(
		template = "templates/generators/foobar.html"
	)

	def get_context(self, context):
		context.parents = [{"name": "foobars", "title": "Los Foobares"}]


@frappe.whitelist()
def update_foobar_desc(foobar, desc):
	#frappe.msgprint('arguments: ' + foobar + ', ' + desc)
	fb = frappe.get_doc("Foobar", foobar)

	if not fb:
		frappe.throw("Foobar '%s' was not initialized." % (foobar))

	if desc == "":
		frappe.throw("Description cannot be blank.")

	fb.foobardesc = desc
	fb.save(ignore_permissions=True)
	fb.clear_cache()

def get_list_context(context):
	context.title = _("Foobars")
	context.introduction = _('Current Foobars')