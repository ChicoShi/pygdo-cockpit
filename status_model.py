"""Small read-only snapshot; never loads personal notes, sessions or credentials."""
from datetime import datetime, timezone
import os
from gdo.base.Trans import t

def snapshot():
    try:
        load = f'{os.getloadavg()[0]:.2f}'
    except (AttributeError, OSError):
        load = t('cp_unavailable')
    return {'observed_at': datetime.now(timezone.utc).isoformat(),
            'load_1m': load, 'scope': t('cp_scope'),
            'connectors': t('cp_connectors_pending'),
            'agents': t('cp_agents_pending'),
            'actions': t('cp_actions_pending')}

def as_text(data):
    return '\n'.join(f'{k}: {v}' for k,v in data.items())
