from frappe import _

def get_data():
	return {
		"gam": {
			"color": "#5a6778",
			"icon": "icon-edit",
			"link": "Report/Works",
			"doctype": "Works",
			"label": _("Works"),
			"type": "report"
		}
	}
