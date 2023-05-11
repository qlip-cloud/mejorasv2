import frappe
from frappe import _

from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
from erpnext.stock.get_item_details import get_item_details


class CustomSalesInvoice(SalesInvoice):

    @frappe.whitelist()
    def qp_refresh_products(self):
        
        if self.get("taxes") and self.taxes:
            frappe.throw(_("Please delete taxes list from document."))

        price_list, price_list_currency = frappe.db.get_values("Price List", {"selling": 1}, ['name', 'currency'])[0]

        for item in self.items:
            if not item.rate:
                args = {
                    'doctype': "Sales Invoice",
                    'item_code': item.item_code,
                    'company': self.company,
                    'customer': self.customer,
                    'selling_price_list': price_list,
                    'price_list_currency': price_list_currency,
                    'plc_conversion_rate': 1.0,
                    'conversion_rate': 1.0
                }
                item_details = get_item_details(args)
                item.rate = item_details.price_list_rate

        self.set_missing_values(for_validate = True)
