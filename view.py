from html import escape
from gdo.core.GDT_String import GDT_String
from gdo.cockpit.status_model import as_text

class CockpitView(GDT_String):
    def with_snapshot(self, data):
        self.data = dict(data)
        self.val(as_text(self.data))
        return self

    def render_html(self):
        d = {k: escape(str(v), quote=True) for k,v in self.data.items()}
        cards = ''.join(f'<article><h2>{title}</h2><p>{d[key]}</p></article>' for title,key in [
            ('Systemlast · 1 Minute','load_1m'),('Connectoren','connectors'),
            ('Agenten','agents'),('Bedienung','actions')])
        return '''<style>.gdo-cockpit{background:#101c26;color:#eef5f6;padding:clamp(20px,4vw,56px);font:17px/1.6 system-ui,sans-serif;border-top:4px solid #58d9cc}.gdo-cockpit h1{font-size:clamp(32px,6vw,56px);margin:0}.gdo-cockpit small{color:#b4c8cf}.gdo-cockpit .cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:20px;margin-top:30px}.gdo-cockpit article{border:1px solid #42616d;padding:22px;border-radius:12px;overflow-wrap:anywhere}.gdo-cockpit h2{font-size:19px;color:#58d9cc}.gdo-cockpit time{overflow-wrap:anywhere}</style>''' + f'''<section class="gdo-cockpit" aria-label="Cockpit"><small>PYGDO / COCKPIT</small><h1>Gemeinsam im Blick.</h1><p>{d['scope']}</p><small>Momentaufnahme: <time>{d['observed_at']}</time></small><div class="cards">{cards}</div><p>Zum Aktualisieren die Seite neu laden.</p></section>'''
