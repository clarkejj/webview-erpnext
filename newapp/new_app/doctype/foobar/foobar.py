# -*- coding: utf-8 -*-
# Copyright (c) 2015, ABC and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.naming import make_autoname

# A controller is a Python class which manages actions on models through differents events:
# before_insert
# validate (before inserting or updating)
# on_update (after saving)
# on_submit (when document is set as submitted)
# on_cancel
# on_trash (before it is about to be deleted)

class Foobar(WebsiteGenerator):
	website = frappe._dict(
		template = "templates/generators/foobar.html",
	)

	def get_context(self, context):
		context.parents = [{"name": "foobars", "title": "Los Foobares"}]

        def validate(self):
#                self.page_title_field = self.foobarid
#                self.page_name = self.name.lower()
		frappe.throw("Foobar '%s' throw exception to invoke log trace example VM:XXX breakpoint in Browser Console..." % (self))
                demo_bad_catch()

        def autoname(self):
#                dt = frappe.get_doc("DocType", "Foobar")
                dt = frappe.get_meta("Foobar")
                key = dt.get("autoname")
                frappe.msgprint('Foobar autoname key: ' + key)
                console.log('Foobar autoname key: ' + key)
                self.name = make_autoname(key)
                print 'Foobar : self.name= ' + self.name
		frappe.throw("Foobar '%s' throw exception to invoke log trace example VM:XXX breakpoint in Browser Console..." % (self))
                raise Error("Foobar '%s' throw exception to invoke log trace example VM:XXX breakpoint in Browser Console..." % (self))

        def demo_bad_catch(self, context):
                try:
                        raise ValueError('represents a hidden bug, do not catch this')
                        raise Exception('This is the exception you expect to handle')
                except Exception as error:
                        print('caught this error: ' + repr(error))

# https://discuss.erpnext.com/t/functions-after-frappe-whitelist/13850/6
#
# Decorator for whitelisting a function and making it accessible via HTTP.
# Standard request will be `/api/method/[path.to.method]`
# :param allow_guest: Allow non logged-in user to access this method.
# Use as:
# @frappe.whitelist()
# def myfunc(param1, param2):
#         pass
# Basically, whitelist method checks permissions, when any request requires to access python method.
# So when you make REST call or want to access method from js you need to make those methods as whitelisted.
# If you are calling a method from python no need to make it as whitelisted.

@frappe.whitelist()
def update_foobar_desc(self, desc):
        print 'update_foobar_desc: self.name= ' + self.name
	frappe.msgprint('arguments: ' + self + ', ' + desc)
	fb = frappe.get_doc("Foobar", self)

	if not fb:
		frappe.throw("Foobar '%s' was not initialized." % (self))

	if desc == "":
		frappe.throw("Description cannot be blank.")

	fb.foobardesc = desc
	fb.save(ignore_permissions=True)
	fb.clear_cache()

# to customize the List View set 
def get_list_context(context):
	context.title = _("Foobars")
	context.introduction = _('Current Foobars')

#         from erpnext.controllers.website_list_for_contact import get_list_context
#         list_context = get_list_context(context)
#         list_context.update({
#                 'show_sidebar': True,
#                 'show_search': True,
#                 'no_breadcrumbs': True,
#                 'title': _('Current Foobars'),
#         })

#         return list_context
