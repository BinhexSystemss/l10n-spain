# Copyright 2018 PESOL - Angel Moya <info@pesol.es>
# Copyright 2019 Tecnativa - Pedro M. Baeza
# Copyright 2014-2023 Binhex - Nicolás Ramos (http://binhex.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    not_in_mod415 = fields.Boolean(
        _("Not included in 415 report"),
        help="If you mark this field, this partner will not be included in "
        "any ATC 415 model report, independently from the total "
        "amount of its operations.",
        default=False,
    )

    @api.model
    def _commercial_fields(self):
        res = super(ResPartner, self)._commercial_fields()
        res += ["not_in_mod415"]
        return res
