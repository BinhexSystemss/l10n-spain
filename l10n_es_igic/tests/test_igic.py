# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo.tests import common, tagged

_logger = logging.getLogger("l10n.igic")


@tagged("post_install_l10n", "-at_install", "post_install")
class TestIgic(common.TransactionCase):
    @classmethod
    def with_context(cls, *args, **kwargs):
        context = dict(args[0] if args else cls.env.context, **kwargs)
        cls.env = cls.env(context=context)
        return cls

    @classmethod
    def _chart_of_accounts_create(cls):
        _logger.debug("Creating chart of account")
        cls.company = cls.env["res.company"].create(
            {"name": "Canary test company", "currency_id": cls.env.ref("base.EUR").id}
        )
        cls.env["account.chart.template"].try_loading(
            "es_pymes_canary", company=cls.company, install_demo=False
        )
        cls.env.ref("base.group_multi_company").write({"users": [(4, cls.env.uid)]})
        cls.env.user.write(
            {"company_ids": [(4, cls.company.id)], "company_id": cls.company.id}
        )
        cls.with_context(company_id=cls.company.id)
        return True

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Create chart
        cls._chart_of_accounts_create()

    def test_01_check_taxes(self):
        # Check taxes
        igic_r_7 = self.env.ref(
            f"account.{self.company.id}_account_tax_template_igic_r_7"
        )
        igic_sop_7 = self.env.ref(
            f"account.{self.company.id}_account_tax_template_igic_sop_7"
        )
        self.assertEqual(igic_r_7.amount, 7.0, "IGIC R tax is not 7%")
        self.assertEqual(igic_sop_7.amount, 7.0, "IGIC SOP tax is not 7%")
