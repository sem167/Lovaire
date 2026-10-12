"""Oogcrème-pagina in Lyvelle-stijl: ondertitel + voordeel-balkjes onder de titel, vette titel, grote prijs, groene knop.
Leest templates__product.oogcreme.json (live versie, zonder commentaarkop) en schrijft hem bijgewerkt terug."""
import json
F = "templates__product.oogcreme.json"
t = json.load(open(F))
det = t["sections"]["main"]["blocks"]["product-details"]
det["blocks"]["lyvelle_intro"] = {"type": "lovaire-pdp-intro", "settings": {
    "subtitle": "Oogcrème | Korean Dark Spot Formula",
    "pill_1_emoji": "🇰🇷", "pill_1_text": "Het K-beauty geheim voor stralende ogen",
    "pill_2_emoji": "👁️", "pill_2_text": "Camoufleert donkere kringen direct",
    "pill_3_emoji": "💧", "pill_3_text": "Verzorgt met calcium, niacinamide & collageen",
    "restyle_section": True, "button_color": "#6ab04c", "button_hover_color": "#5c9d40"}, "blocks": {}}
det["blocks"].pop("vendor", None)
order = [k for k in det["block_order"] if k not in ("vendor", "lyvelle_intro")]
order.insert(order.index("title") + 1, "lyvelle_intro")
det["block_order"] = order
det["settings"]["gap"] = 18
json.dump(t, open(F, "w"), ensure_ascii=False, indent=2)
print(det["block_order"])
