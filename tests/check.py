import importlib.util,sys
from pathlib import Path
from unittest.mock import patch
from gdo.base.Application import Application
from gdo.base.Render import Mode
Application.mode(Mode.render_txt)
p=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('gdo.cockpit',p/'__init__.py',submodule_search_locations=[str(p)])
m=importlib.util.module_from_spec(s);sys.modules['gdo.cockpit']=m;s.loader.exec_module(m)
from gdo.cockpit.status_model import snapshot
from gdo.cockpit.view import CockpitView
from gdo.cockpit.method.status import status
from gdo.cockpit.method.site import site
v=snapshot();assert set(v)=={'observed_at','load_1m','scope','connectors','agents','actions'}
v['scope']='<script>alert(1)</script>'
html=CockpitView('result').with_snapshot(v).render_html();assert '<script>' not in html and '&lt;script&gt;' in html
for cls in [status,site]:
 cmd=cls();assert cmd.gdo_user_type()=='member' and cmd.gdo_needs_authentication() and cmd.gdo_user_permission()=='staff'
 with patch.object(cls,'gdo_module') as mod:
  mod.return_value.get_config_value.return_value=False
  assert 'deaktiviert' in cmd.gdo_execute().get_val()
  mod.return_value.get_config_value.return_value=True
  result=cmd.gdo_execute();assert 'Noch kein' in result.get_val() and 'Gemeinsam' in result.render_html()
assert site.gdo_trigger()=='' and site().gdo_connectors()=='web'
assert status.gdo_trigger()=='cockpit.status'
print('PASS: snapshot, escaping, permission declarations, shared web/chat, disabled/enabled adapter. No live authentication tested.')
if '--preview' in sys.argv:
 Path('/tmp/cockpit-preview.html').write_text('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'+CockpitView('result').with_snapshot(snapshot()).render_html())
