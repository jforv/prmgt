# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "lifestyle"
app_title = "Lifestyle"
app_publisher = "Verynice SRL"
app_description = "Condominium Management app"
app_icon = "octicon octicon-home"
app_color = "grey"
app_email = "jforvil@verynice.com.do"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/lifestyle/css/lifestyle.css"
# app_include_js = "/assets/lifestyle/js/lifestyle.js"

# include js, css files in header of web template
# web_include_css = "/assets/lifestyle/css/lifestyle.css"
# web_include_js = "/assets/lifestyle/js/lifestyle.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "lifestyle.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "lifestyle.install.before_install"
# after_install = "lifestyle.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lifestyle.notifications.get_notification_config"

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
# 		"lifestyle.tasks.all"
# 	],
# 	"daily": [
# 		"lifestyle.tasks.daily"
# 	],
# 	"hourly": [
# 		"lifestyle.tasks.hourly"
# 	],
# 	"weekly": [
# 		"lifestyle.tasks.weekly"
# 	]
# 	"monthly": [
# 		"lifestyle.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "lifestyle.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lifestyle.event.get_events"
# }

