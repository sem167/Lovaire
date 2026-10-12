"""Twee video's naast elkaar direct onder het koopblok van de oogcrème-pagina (sectie lovaire-video-duo)."""
import json
F = "templates__product.oogcreme.json"
t = json.load(open(F))
t["sections"]["videos"] = {"type": "lovaire-video-duo", "settings": {
    "heading": "Zie de Calcium Oogcrème zelf in actie 💕", "background": "#ffffff", "padding_top": 40, "padding_bottom": 48}}
order = [k for k in t["order"] if k != "videos"]
order.insert(order.index("main") + 1, "videos")
t["order"] = order
json.dump(t, open(F, "w"), ensure_ascii=False, indent=2)
print(t["order"])
