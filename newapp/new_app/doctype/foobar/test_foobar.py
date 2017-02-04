# -*- coding: utf-8 -*-
# Copyright (c) 2017, aproposcomputing.com
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest
import datetime


# test_records = frappe.get_test_records('Foobar')
# test_dependencies = ["Product Bundle"]

class TestFoobar(unittest.TestCase):

        def setUp(self):
                pass
                # make_earning_salary_component(["Basic Salary", "Allowance", "HRA"])
                # make_deduction_salary_component(["Professional Tax", "TDS"])

                # for dt in ["Leave Application", "Leave Allocation", "Salary Slip"]:
                #         frappe.db.sql("delete from `tab%s`" % dt)

                # self.make_holiday_list()

                # frappe.db.set_value("Company", erpnext.get_default_company(), "default_holiday_list", "Salary Slip Test Holiday List")


        def tearDown(self):
                pass
                # frappe.db.set_value("HR Settings", None, "include_holidays_in_total_working_days", 0)
                # frappe.set_user("Administrator")

        def test_create_Foobar(self):
                # setup
#                from frappe.test_runner import print_mandatory_fields
#                print_mandatory_fields('Foobar')
		fb = frappe.get_doc(dict(doctype='Foobar', foobarid='abc123', foobardesc='this is a create Foobar test instance',
			foobardate=datetime.datetime.now()))
#                fb = fb.insert()
#		self.assertEquals(fb.name, 'Foobar-1')
#		self.assertEquals(fb.foobardesc, 'new description')
#                fb.foobardesc='new description'
#		fb = fb.save()

                # execute system under test
                fb.insert()

                # assert
                self.assertEquals(fb.doctype, "Foobar")
		self.assertEquals(fb.foobarid, 'abc123')
		self.assertEquals(fb.foobardesc, 'this is a Foobar create test instance')

                # teardown
#                fb.delete()

        def test_read_Foobar(self):
                # setup

                # execute system under test
		fb = frappe.get_doc('Foobar', "Foobar-1")

                # assert
                self.assertEquals(fb.doctype, "Foobar")
		self.assertEquals(fb.foobarid, 'abc123')
		self.assertEquals(fb.foobardesc, 'this is Foobar doc test instance')

        def test_update_Foobar(self):
                # setup
		fb = frappe.get_doc(dict(doctype='Foobar', foobarid='abc123', foobardesc='this is Foobar doc test instance',
			foobardate=datetime.datetime.now()))

		self.assertEquals(fb.foobardesc, 'this is Foobar doc test instance')
                fb.foobardesc='new description'

                # execute system under test
		fb.save()

                # assert
		fb = frappe.get_doc('Foobar', "Prompt00003")

                self.assertEquals(fb.doctype, "Foobar")
		self.assertEquals(fb.foobarid, 'abc123')
		self.assertEquals(fb.foobardesc, 'this is Foobar doc test instance')

        def test_delete_Foobar(self):
                # setup
		fb = frappe.get_doc('Foobar', "Foobar-2")

                # execute system under test
                fb = fb.delete()

                # assert
                self.assertIsNone(fb)
                with self.assertRaises(frappe.DoesNotExistError): frappe.get_doc('Foobar', "Foobar-2")


        def test_Foobar_autoname_spec(self):
                dt = frappe.get_doc("DocType", "Foobar")
                key = dt.get("autoname")
                frappe.msgprint('Foobar autoname key: ' + key)
#                console.log('Foobar autoname key: ' + key)
                self.assertEquals(key, "Foobar-.#")
		fb = frappe.get_doc('Foobar', "Foobar-2")
                print 'Foobar : fb.name= ' + fb.name
                fb.demo_bad_catch()
