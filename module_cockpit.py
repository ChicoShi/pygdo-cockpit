from gdo.base.GDO_Module import GDO_Module
from gdo.core.GDT_Bool import GDT_Bool

class module_cockpit(GDO_Module):
    def gdo_module_config(self):
        return [GDT_Bool('cockpit_enabled').not_null().initial('0')]
