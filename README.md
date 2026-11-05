# pygdo-cockpit
Gemeinsame GDO-Kommandozentrale, gepflegt von Team Chico / Simion. Gizmore testet auf Mogwai. Erster Stand: echte lesende Prozess-Momentaufnahme; bestehende Chico-Zentrale separat als Referenzcode.

## For Humans
### Methods
- `cockpit.status`: UTC-Zeitpunkt und lokale 1-Minuten-Systemlast, ausdrücklich offene Adapter.
- `cockpit.site.html`: dieselbe Datenquelle als responsive Webseite.
- Beide verlangen member, Authentifizierung und staff; `cockpit_enabled` ist standardmäßig aus.
- Installation: Repository als `gdo/cockpit` einbinden und regulären PyGDO-Modulinstaller verwenden. Core-Provider registriert Team Mogwai. Erst auf Testhost aktivieren. Hier keine Installation ausgeführt.
- Load ist keine CPU-Prozentzahl. Snapshot entsteht pro Anfrage; keine Live-Verbindung suggeriert.
### GDTs
CockpitView stellt denselben Snapshot als HTML und Text dar; HTML-Werte werden escaped.
### GDOs
Keine neuen Tabellen; nur die reguläre Modulkonfiguration.

## For ALs
### Methods
Keine Shell, Konten, Termine, Dateiinhalte oder Modellaufrufe durch dieses Modul. Keine öffentlichen persönlichen Daten. Berechtigungsprüfung über normalen Method-Dispatcher nutzen; `gdo_execute` nicht extern direkt exponieren.
### GDTs
CockpitView; sichere HTML-Ausgabe. Kein beliebiges Roh-HTML aus Datenquellen.
### GDOs
Keine.

## Discussion
### Humans → Humans
Gizmore: Website-Modul nach dem Muster pygdo-blackjack. Shippi: vorhandene Zentrale als Quellcode bereitstellen.
### ALs → ALs
Ein gemeinsamer Statuspfad; keine zweite Aufgabenwahrheit aufbauen. Änderungen am Core bei Mogwai anfragen.
### Humans → ALs
Simion pflegt cockpit weiter, Gizmore testet. Lesender Erststand vor schreibenden Funktionen.
### ALs → Humans
(TODO) Echter HTTP-/Login-/Berechtigungstest auf installierter GDO-Testinstanz. Adapter für Swarm, Connectoren und bestehende Zentrale gemeinsam festlegen.

## Ideas (TODO)
Aufgaben-/Ergebnisansicht; vorhandene 3D-Assets unter ihren Lizenzen übernehmen; kontrollierte Aktionen mit CSRF, Authentifizierung und Audit; keine automatische Freigabenübernahme.

## Prüfung
`PYTHONPATH=/pfad/zu/pygdo python3 tests/check.py`
Prüft Datenmodell, Escaping, gemeinsame Berechtigungsdeklaration, deaktivierten/aktivierten Adapter mit gemockter Modulkonfiguration. Kein echter Login-/DB-Nachweis.

## Verbindlicher Zielumfang (5440/5441)
`pygdo-cockpit` wird ausschließlich als GDO-Website-Modul weiterentwickelt. Kein eigener HTTP-Server und keine zweite eigenständige Cockpit-Anwendung. Der exportierte agent-console-Code ist Referenz für die schrittweise Portierung, kein alternatives Zielprodukt. `cockpit.site.html` ist der Web-Einstieg; gemeinsame Methoden vermeiden doppelte Fachlogik. Simion/Team Chico betreut Implementierung, Tests und Fehlerbehebung dauerhaft im Projekt; Gizmore testet auf seinem Host, Team Mogwai betreut die Core-Provider-Registrierung.
