from gdo.base.Method import Method
from gdo.core.GDT_String import GDT_String
from gdo.cockpit.status_model import snapshot
from gdo.cockpit.view import CockpitView

class status(Method):
    @classmethod
    def gdo_trigger(cls): return 'cockpit.status'
    def gdo_user_type(self): return 'member'
    def gdo_needs_authentication(self): return True
    def gdo_user_permission(self): return 'staff'
    def gdo_transactional(self): return False
    def gdo_execute(self):
        if not self.gdo_module().get_config_value('cockpit_enabled'):
            return GDT_String('result').val('Cockpit ist deaktiviert.')
        return CockpitView('result').with_snapshot(snapshot())
