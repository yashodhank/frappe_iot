# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version
from frappe import _

app_name = "iot"
app_title = "IOT"
app_publisher = "Dirk Chang"
app_description = "App for SymLink IOT"
app_icon = "octicon octicon-cloud-upload"
app_color = "grey"
app_email = "dirk.chang@symid.com"
app_license = "MIT"
source_link = "https://github.com/srdgame/frappe_iot"

error_report_email = "dirk.chang@symid.com.com"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/iot/css/iot.css"
# app_include_js = "/assets/iot/js/iot.js"

# include js, css files in header of web template
# web_include_css = "/assets/iot/css/iot.css"
# web_include_js = "/assets/iot/js/iot.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "iot_home"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "iot.utils.get_home_page"

# Website Route Rules
website_route_rules = [
	{"from_route": "/iot_enterprises", "to_route": "IOT Enterprise"},
	{"from_route": "/iot_enterprises/<path:name>", "to_route": "iot_enterprise",
		"defaults": {
			"doctype": "IOT Enterprise",
			"parents": [{"title": _("IOT Enterprise"), "name": "iot_enterprises"}]
		}
	},
	{"from_route": "/iot_employee_groups", "to_route": "IOT Employee Group"},
	{"from_route": "/iot_employee_groups/<path:name>", "to_route": "iot_employee_group",
		"defaults": {
			"doctype": "IOT Employee Group",
			"parents": [{"title": _("IOT Employee Group"), "name": "iot_employee_groups"}]
		}
	},
	{"from_route": "/iot_device_bunch_codes", "to_route": "IOT Device Bunch"},
	{"from_route": "/iot_device_bunch_codes/<path:name>", "to_route": "iot_device_bunch",
		"defaults": {
			"doctype": "IOT Device Bunch",
			"parents": [{"title": _("IOT Device Bunch"), "name": "iot_device_bunch_codes"}]
		}
	},
	{"from_route": "/iot_devices", "to_route": "IOT Device"},
	{"from_route": "/iot_devices/<path:name>", "to_route": "iot_device",
		"defaults": {
			"doctype": "IOT Device",
			"parents": [{"title": _("IOT Device"), "name": "iot_devices"}]
		}
	},
	{"from_route": "/iot_users", "to_route": "IOT User"},
	{"from_route": "/iot_users/<path:name>", "to_route": "iot_user",
		"defaults": {
			"doctype": "IOT User",
			"parents": [{"title": _("IOT User"), "name": "iot_users"}]
		}
	},
]

portal_menu_items = [
	{"title": _("IOT Enterprises"), "route": "/iot_enterprises", "reference_doctype": "IOT Enterprise", "role": "IOT Manager"},
	{"title": _("IOT Enterprise"), "route": "/iot_enterprise", "role": "IOT User"},
	{"title": _("IOT Devices"), "route": "/iot_devices", "reference_doctype": "IOT Enterprise", "role": "IOT User"},
	{"title": _("IOT Devices Map"), "route": "/iot_device_map", "role": "IOT User"},
	{"title": _("IOT Account"), "route": "/iot_me"}
]

doc_events = {
	"User": {
		"after_insert": "iot.iot.controllers.user_hooks.after_insert",
	},
}

# Top bars
website_context = {
	"favicon": 	"/assets/img/frappe-bird-white.png",
#	"top_bar_items": [
#		{"label": "IOT Enterprise", "url": "/iot_enterprises", "right": 1},
#		{"label": "IOT Devices", "url": "/iot_devices", "right": 1},
#		{"label": "IOT Account", "url": "/iot_me", "right": 1},
#		{"label": "SymLink", "url": 'https://www.symid.com', "right": 1}
#	]
}

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "iot.install.before_install"
# after_install = "iot.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "iot.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

#permission_query_conditions = {
#	"IOT Device": "iot.iot.doctype.iot_device.iot_device.get_permission_query_conditions",
#}

# Dirk: has permission will replace system's permission checking for DocType
#has_permission = {
#	"IOT Device": "iot.iot.doctype.iot_device.iot_device.has_permission",
#	"IOT Device Bunch": "iot.iot.doctype.iot_device_bunch.iot_device_bunch.has_permission",
#}

has_website_permission = {
	"IOT Enterprise": "iot.iot.doctype.iot_enteprise.iot_enterprise.has_website_permission",
	"IOT Device": "iot.iot.doctype.iot_device.iot_device.has_website_permission",
	"IOT Device Bunch": "iot.iot.doctype.iot_device_bunch.iot_device_bunch.has_website_permission",
	"IOT User": "iot.iot.doctype.iot_user.iot_user.has_website_permission",
}

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
# 		"iot.tasks.all"
# 	],
# 	"daily": [
# 		"iot.tasks.daily"
# 	],
# 	"hourly": [
# 		"iot.tasks.hourly"
# 	],
# 	"weekly": [
# 		"iot.tasks.weekly"
# 	]
# 	"monthly": [
# 		"iot.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "iot.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "iot.event.get_events"
# }

