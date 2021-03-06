# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
	'name': "Imagen del Producto en lineas de venta",
	'version': "15.0.0.2",
	'category': "Sales",
	'license': "AGPL-3",
	'summary': "Mostrar imagen del producto en las lineas del pedido de venta así como en reporte.",
	'description': """
	
			Mostrar imagen del producto en las lineas de venta así como en reportes.
	""",
	'author': "Alfonso Gonzalez (alfonso@ptree.com.mx)",
    'website': "https://ptree.com.mx/",
    'depends': ['base', 'sale_management'],
	'sequence': "-10",
	'data': [
			'report/sale_order_report.xml',
			'views/view_sale_order.xml',
			],
	'demo': [],
	'installable': True,
	'auto_install': False,
	'application': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
