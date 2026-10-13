"""30 dagen retour (ongeopende producten) en 24/7 Nederlandse klantenservice in alle themabestanden.
Gebruik: python3 retour30_service247.py <json met theme.files.nodes> <uitvoermap>"""
import json, sys, re, os
src, out = sys.argv[1], sys.argv[2]
nodes = json.load(open(src))["data"]["theme"]["files"]["nodes"]
R = [
  ("Je kunt je bestelling binnen 14 dagen na ontvangst retourneren.",
   "Je kunt ongeopende producten binnen 30 dagen na ontvangst retourneren."),
  ("We reageren op werkdagen tussen 09:00 en 17:00.", "Onze Nederlandse klantenservice is 24/7 voor je bereikbaar."),
  ("Ons team reageert op werkdagen tussen 09:00 en 17:00.", "Onze Nederlandse klantenservice is 24/7 voor je bereikbaar."),
  ("\"title\": \"Persoonlijke service\",\n            \"text\": \"We zijn er voor je op ma–vr, 09:00–17:00.\"",
   "\"title\": \"24/7 klantenservice\",\n            \"text\": \"Nederlandse klantenservice, dag en nacht bereikbaar.\""),
  ("We zijn er voor je op ma–vr, 09:00–17:00.", "Nederlandse klantenservice, dag en nacht bereikbaar."),
  ("Ma–vr: 09:00–17:00<br/>Za: 10:00–14:00<br/>Zo: gesloten", "24/7 bereikbaar<br/>Nederlandstalige klantenservice"),
  ("\"default\": \"Persoonlijke service\" },\n    { \"type\": \"text\", \"id\": \"item_4_text\", \"label\": \"Voordeel 4 – tekst\", \"default\": \"Ma–vr 09:00–17:00\" }",
   "\"default\": \"24/7 klantenservice\" },\n    { \"type\": \"text\", \"id\": \"item_4_text\", \"label\": \"Voordeel 4 – tekst\", \"default\": \"Nederlands, dag en nacht\" }"),
  ("\"default\": \"14 dagen retour\"", "\"default\": \"30 dagen retour\""),
]
HDR = re.compile(r"^/\*.*?\*/\s*", re.S)
changed = {}
for n in nodes:
    c = (n.get("body") or {}).get("content")
    if c is None: continue
    new = c
    for a, b in R: new = new.replace(a, b)
    if new != c:
        if n["filename"].endswith(".json"):
            new = json.dumps(json.loads(HDR.sub("", new)), ensure_ascii=False, separators=(",", ":"))
        changed[n["filename"]] = new
left = [f for f, c in changed.items() if re.search(r"14 dagen|09:00|ma–vr|Ma–vr", c)]
print("gewijzigd:", len(changed), "| nog oude tekst in:", left)
os.makedirs(out, exist_ok=True)
for f, c in changed.items():
    open(os.path.join(out, f.replace("/", "__")), "w").write(c)
    print(f, len(c))
