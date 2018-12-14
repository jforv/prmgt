# -*- coding: utf-8 -*-
# Copyright (c) 2018, Verynice SRL and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import cint, cstr, getdate
import dateutil
from frappe.model.naming import make_autoname

class UnitUser(Document):
	def after_insert(self):
		create_customer(self)
		create_user(self)

	def on_update(self):
		self.add_as_website_user()

	def add_as_website_user(self):
		if(self.email):
			if not frappe.db.exists ("User", self.email):
				user = frappe.get_doc({
					"doctype": "User",
					"first_name": self.patient_name,
					"email": self.email,
					"user_type": "Website User"
				})
				user.flags.no_welcome_email = False
				user.flags.ignore_permissions = True
				user.add_roles("Customer")

def create_customer(doc):
	customer_group = frappe.get_value("Selling Settings", None, "customer_group")
	territory = frappe.get_value("Selling Settings", None, "territory")
	if not (customer_group and territory):
		customer_group = "Commercial"
		territory = "All Territories"
		frappe.msgprint(_("Please set default customer group and territory in Selling Settings"), alert=True)
	customer = frappe.get_doc({"doctype": "Customer",
	"customer_name": doc.full_name,
	"customer_group": customer_group,
	"territory" : territory,
	"customer_type": "Individual"
	}).insert(ignore_permissions=True)
	frappe.db.set_value("Unit User", doc.full_name, "customer", customer.name)
	frappe.msgprint(_("Customer {0} is created.").format(customer.name), alert=True)

def create_user(doc):
	# customer_group = frappe.get_value("Selling Settings", None, "customer_group")
	# territory = frappe.get_value("Selling Settings", None, "territory")
	name = doc.full_name.split()
	if not (doc.email and name[0]):
		frappe.msgprint(_("Please set email and name"), alert=True)
	user = frappe.get_doc({"doctype": "User",
	"username": name[0]+name[-1].title(),
	"first_name": name[0],
	"last_name": name[-1],
	"email": doc.email,
	"send_welcome_email": False
	}).insert(ignore_permissions=True)
	# frappe.db.set_value("Unit User", doc.full_name, "First Name", name[0])
	frappe.msgprint(_("User {0} is created.").format(user.first_name), alert=True)

def make_invoice(unit_user, company):
	sales_invoice = frappe.new_doc("Sales Invoice")
	sales_invoice.customer = frappe.get_value("Unit User", unit_user, "customer")
	sales_invoice.due_date = getdate()
	sales_invoice.company = company
	sales_invoice.is_pos = '0'
	sales_invoice.debit_to = get_receivable_account(company)

	item_line = sales_invoice.append("items")
	item_line.item_name = "Alquiler"
	item_line.description = "Monthly Fee"
	item_line.qty = 1
	item_line.uom = "Month"
	item_line.conversion_factor = 1
	item_line.income_account = get_income_account(None, company)
	# item_line.rate = frappe.get_value("Healthcare Settings", None, "registration_fee")
	item_line.amount = item_line.rate
	sales_invoice.set_missing_values()
	return sales_invoice