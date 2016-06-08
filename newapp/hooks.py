# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "newapp"
app_title = "New App"
app_publisher = "ABC"
app_description = "To demonstrate app creation using Frappe"
app_icon = "octicon octicon-package"
app_color = "#DA261D"
app_email = "a@b.c"
app_version = "0.0.1"
app_license = "GPL v3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/newapp/css/newapp.css"
# app_include_js = "/assets/newapp/js/newapp.js"

# include js, css files in header of web template
# web_include_css = "/assets/newapp/css/newapp.css"
# web_include_js = "/assets/newapp/js/newapp.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "newapp.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
website_generators = ["Foobar"]

# Installation
# ------------

# before_install = "newapp.install.before_install"
# after_install = "newapp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "newapp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"newapp.tasks.all"
# 	],
# 	"daily": [
# 		"newapp.tasks.daily"
# 	],
# 	"hourly": [
# 		"newapp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"newapp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"newapp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "newapp.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "newapp.event.get_events"
# }

