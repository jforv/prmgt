// Copyright (c) 2018, Verynice SRL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Unit User', {
	refresh: function(frm) {
		console.log('refreshed UNit');
		if (frm.doc.user_status=='Owner'|| frappe.user.has_role('Accounts Manager')) {
			frm.set_df_property('user_status', 'read_only', false);
			frm.add_custom_button(__('Sales Invoice'), function () {
				btn_create_sales_invoice(frm);
			}, "Create");
		}
	}
});

var btn_create_sales_invoice = function (frm) {
	// eval:(doc.user_type=='Tenant' || doc.user_type=='Owner')
	if (!frm.doc.name) {
		frappe.throw("Please save the User first");
	}
	frappe.route_options = {
		"unit_user": frm.doc.name,
	};
	frappe.new_doc("Sales Invoice");
};
