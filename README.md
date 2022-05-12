# pwCard
### Mit Python eine PDF Passwortkarte erstellen (getestet mit Python 3.10)
YT Quelle: [Passwortkarten und wie man sie mit Python erzeugen kann](https://www.youtube.com/watch?v=jMu5olgIuOE) von Florian Dalwigk.

![pwCard_demo_bitte-nicht-nutzen](https://user-images.githubusercontent.com/1485851/167740263-5ba52786-42c4-4c31-93b9-917525cca4be.jpg)
#### Screenshot als Demo, bitte NICHT nutzen!!!

"Test-1" wäre dann: 5AP_RRXG1a#6w)FrTM

(die Spalte XZ1 nutze ich in diesem Beispiel auch für Zahlen)

---

**pwCard** ist eine ausführbare Datei welche aus pwCard.py für Linux erstellt wurde (ca. 11MB). In dieser Datei sind alle Abhängigkeiten enthalten und muss nur als ausführbar markiert werden. Es ist kein sudo notwendig! Getestet mit Manjaro 21.2.6, Ubuntu 22.04 und Mint 21. Nach dem Download solltet ihr die SHA1 Prüfsumme checken.
Ausführen z.B.:
- &nbsp;&nbsp;./pwCard &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (ohne Sonderzeichen)
- &nbsp;&nbsp;./pwCard 1 &nbsp;&nbsp;&nbsp;&nbsp; (mit Sonderzeichen - krass)
- &nbsp;&nbsp;./pwCard 2 &nbsp;&nbsp;&nbsp;&nbsp; (mit Sonderzeichen - normal)
