# -*- coding: utf-8 -*-
##############################################################################
#
#     Author:  Fekete Mihai <mihai.fekete@forbiom.eu>
#    Copyright (C) 2014 FOREST AND BIOMASS SERVICES ROMANIA SA (http://www.forbiom.eu).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Partner create by VAT",
    "version" : "1.0",
    "author" : "FOREST AND BIOMASS SERVICES ROMANIA	",
    "website": "http://www.forbiom.eu",
    "category" : "Hidden",
    "depends": ['l10n_ro','base_vat'],
    "description": """
Partner create by vat from Mfinante for Romanian Companies or Vies site for Euroipean one
------------------------------------------


    """,

    'data': ['res_partner_view.xml',
             ],
    'installable': True,
    'auto_install': True,
}
