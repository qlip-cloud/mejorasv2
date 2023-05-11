frappe.ui.form.on('Sales Invoice', {
	refresh: function(frm) {
		if (frm.doc.docstatus===0) {
			frm.add_custom_button(__("Load Products Details"), function() {
				frappe.confirm(__("This action will updated product list. It cannot be undone. Are you certain?"), function() {
					frappe.call({
						doc: frm.doc,
						method: "qp_refresh_products",
						args:{},
						callback: function() {
							frm.trigger("validate");
							frm.refresh_fields();
							frappe.show_alert("Product list updated!");
						}
					});
				});
			});
		}
	}
})
