from frappe import _

def get_data():
	return {
		'heatmap': False,
		'heatmap_message': _('This is based on transactions against this Patient. See timeline below for details'),
		# 'fieldname': 'tenant',
		'transactions': [
			{
				'label': _('Facility and Request'),
				'items': ['Facility Booking', 'Facility', 'Special Request']
			},
			{
				'label': _('Sales Invoice and Complaint'),
 				'items': ['Sales Invoice', 'Item']
			}
		]
	}