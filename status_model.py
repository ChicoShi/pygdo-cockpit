"""Small read-only snapshot; never loads personal notes, sessions or credentials."""
from datetime import datetime, timezone
import os

def snapshot():
    try:
        load = f'{os.getloadavg()[0]:.2f}'
    except (AttributeError, OSError):
        load = 'nicht verfügbar'
    return {'observed_at': datetime.now(timezone.utc).isoformat(),
            'load_1m': load, 'scope': 'Dieser GDO-Prozess',
            'connectors': 'Noch kein Connector-Statusadapter angebunden',
            'agents': 'Noch kein Agenten-Statusadapter angebunden',
            'actions': 'Lesender Erststand; keine Steueraktionen'}

def as_text(data):
    return '\n'.join(f'{k}: {v}' for k,v in data.items())
