from gdo.cockpit.method.status import status

class site(status):
    """Same data and permission declarations as the chat method."""
    @classmethod
    def gdo_trigger(cls): return ''
    def gdo_connectors(self): return 'web'
