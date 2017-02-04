## New App

To demonstrate app creation using Frappe

#### License

GPL v3

This is a fork from gaurav-naik/webview-erpnext (commit date 8 Jun 2016)

newapp is an example of a custom app separate from frappe and erpnext app.

Install instructions and notes - two steps to install:

1) First, download newapp from github remote repository to frappe-bench local with this:

frappe@erpnext:~/frappe-bench$ bench get-app --branch develop webview-erpnext https://github.com/gaurav-naik/webview-erpnext.git

2) Second, to complete the install login to ERPNext to access and run the App Installer:

Setup -> App Installer install 'New App' from Category 'Not set'

frappe@erpnext:~/frappe-bench$ bench list-apps
frappe
erpnext
newapp

Note that newapp installs and runs from erpnext without any apparent reference links to it from erpnext, as this grep search confirms:

frappe@erpnext:~/frappe-bench$ find . -name *.py | xargs grep 'New App'
./apps/newapp/newapp/hooks.py:app_title = "New App"
./apps/newapp/newapp/config/desktop.py:	       "module_name": "New App",
./apps/newapp/newapp/config/desktop.py:	       		      	   "label": _("New App")
./apps/newapp/newapp/config/docs.py:				   context.brand_html = "New App"

frappe@erpnext:~/frappe-bench$ find . -name *.py | xargs grep 'New App'
./apps/newapp/newapp/hooks.py:app_title = "New App"
./apps/newapp/newapp/config/desktop.py:	       "module_name": "New App",
./apps/newapp/newapp/config/desktop.py:	       		      	   "label": _("New App")
./apps/newapp/newapp/config/docs.py:				   context.brand_html = "New App"
frappe@erpnext:~/frappe-bench$ find . -name *.py | xargs grep 'newapp'
./apps/newapp/newapp/hooks.py:app_name = "newapp"
./apps/newapp/newapp/hooks.py:# app_include_css = "/assets/newapp/css/newapp.css"
./apps/newapp/newapp/hooks.py:# app_include_js = "/assets/newapp/js/newapp.js"
./apps/newapp/newapp/hooks.py:# web_include_css = "/assets/newapp/css/newapp.css"
./apps/newapp/newapp/hooks.py:# web_include_js = "/assets/newapp/js/newapp.js"
./apps/newapp/newapp/hooks.py:# get_website_user_home_page = "newapp.utils.get_home_page"
./apps/newapp/newapp/hooks.py:# before_install = "newapp.install.before_install"
./apps/newapp/newapp/hooks.py:# after_install = "newapp.install.after_install"
./apps/newapp/newapp/hooks.py:# notification_config = "newapp.notifications.get_notification_config"
./apps/newapp/newapp/hooks.py:# 		      "newapp.tasks.all"
./apps/newapp/newapp/hooks.py:#				"newapp.tasks.daily"
./apps/newapp/newapp/hooks.py:#					"newapp.tasks.hourly"
./apps/newapp/newapp/hooks.py:#						"newapp.tasks.weekly"
./apps/newapp/newapp/hooks.py:#							"newapp.tasks.monthly"
./apps/newapp/newapp/hooks.py:# before_tests = "newapp.install.before_tests"
./apps/newapp/newapp/hooks.py:# 	     "frappe.desk.doctype.event.event.get_events": "newapp.event.get_events"
./apps/newapp/newapp/config/docs.py:# source_link = "https://github.com/[org_name]/newapp"
./apps/newapp/newapp/config/docs.py:# docs_base_url = "https://[org_name].github.io/newapp"
./apps/newapp/setup.py:		      name='newapp',


To add a new Foobar instance (in Setup -> New App -> Foobar) this traceback occurred:

Traceback (most recent call last):
  File "/home/frappe/frappe-bench/apps/frappe/frappe/app.py", line 55, in application
    response = frappe.handler.handle()
  File "/home/frappe/frappe-bench/apps/frappe/frappe/handler.py", line 19, in handle
    execute_cmd(cmd)
  File "/home/frappe/frappe-bench/apps/frappe/frappe/handler.py", line 40, in execute_cmd
    ret = frappe.call(method, **frappe.form_dict)
  File "/home/frappe/frappe-bench/apps/frappe/frappe/__init__.py", line 897, in call
    return fn(*args, **newargs)
  File "/home/frappe/frappe-bench/apps/frappe/frappe/desk/form/save.py", line 22, in savedocs
    doc.save()
  File "/home/frappe/frappe-bench/apps/frappe/frappe/model/document.py", line 223, in save
    return self._save(*args, **kwargs)
  File "/home/frappe/frappe-bench/apps/frappe/frappe/model/document.py", line 242, in _save
    self.insert()
  File "/home/frappe/frappe-bench/apps/frappe/frappe/model/document.py", line 184, in insert
    self.set_new_name()
  File "/home/frappe/frappe-bench/apps/frappe/frappe/model/document.py", line 322, in set_new_name
    set_new_name(self)
  File "/home/frappe/frappe-bench/apps/frappe/frappe/model/naming.py", line 38, in set_new_name
    doc.run_method("autoname")
  File "/home/frappe/frappe-bench/apps/frappe/frappe/model/document.py", line 651, in run_method
    out = Document.hook(fn)(self, *args, **kwargs)
  File "/home/frappe/frappe-bench/apps/frappe/frappe/model/document.py", line 858, in composer
    return composed(self, method, *args, **kwargs)
  File "/home/frappe/frappe-bench/apps/frappe/frappe/model/document.py", line 841, in runner
    add_to_return_value(self, fn(self, *args, **kwargs))
  File "/home/frappe/frappe-bench/apps/frappe/frappe/model/document.py", line 645, in 
    fn = lambda self, *args, **kwargs: getattr(self, method)(*args, **kwargs)
  File "/home/frappe/frappe-bench/apps/frappe/frappe/website/website_generator.py", line 25, in autoname
    self.name = self.scrub(self.get(self.website.page_title_field or "title"))
  File "/home/frappe/frappe-bench/apps/frappe/frappe/website/website_generator.py", line 52, in scrub
    return cleanup_page_name(text).replace('_', '-')
AttributeError: 'NoneType' object has no attribute 'replace'

Given Foobar's autoname spec Foobar-.#, the Frappe domain works as expected for Foobar as a subclass of Document (ie generates the name Foobar-1 etc) but not for the case of WebsiteGenerator.  This is a design oversight, the workaround is for Foobar to implement autoname() in the controller by calling auto_make().

test_foobar.py includes basic CRUD tests.  When a test is run from the console terminal command line note that the ERPNext GUI View List for Foobar is updated in the case of insert but not update or delete.  Here are example command line tests:

frappe@erpnext:~/frappe-bench/apps/newapp$ bench run-tests --doctype Foobar --test test_create_Foobar
frappe@erpnext:~/frappe-bench/apps/newapp$ bench run-tests --doctype Foobar --test test_Foobar_autoname_spec

