"""Lyvelle-achtige stijl (alleen vormgeving): blush-vlakken, taupe labels, links uitgelijnde hero."""
import json
from build import text, button, ordered

def load(n): return json.load(open(n))
def save(n, d): json.dump(d, open(n, "w"), ensure_ascii=False, indent=2)

def walk(node):
    if isinstance(node, dict):
        if node.get("type") == "text" and node.get("settings", {}).get("type_preset") == "h6":
            node["settings"]["color"] = "var(--color-primary)"
        for v in node.values(): walk(v)
    elif isinstance(node, list):
        for v in node: walk(v)

idx = load("templates__index.json")
S = idx["sections"]
S["hero"] = {"type": "hero", "name": "Hero", **ordered([
    ("eyebrow", text("<p>—— LOVAIRE</p>", preset="h6")),
    ("heading", text("<h1>Beauty essentials voor jouw glow, elke dag</h1>", preset="h1", max_width="narrow",
                     font="var(--font-heading--family)", color="var(--color-foreground-heading)")),
    ("subtext", text("<p>Make-up, huid- en haarverzorging die je echt gebruikt. Altijd gratis verzending.</p>", max_width="narrow")),
    ("cta", button("Shop nu →", "shopify://collections/all")),
]), "settings": {"content_direction": "column", "vertical_on_mobile": True,
                 "horizontal_alignment_flex_direction_column": "flex-start",
                 "vertical_alignment_flex_direction_column": "center", "gap": 20,
                 "section_width": "page-width", "section_height": "custom", "section_height_custom": 60,
                 "color_scheme": "scheme-5", "toggle_overlay": False,
                 "padding-block-start": 64, "padding-block-end": 64}}
m = S["marquee"]
m["settings"]["color_scheme"] = "scheme-5"
m["settings"]["padding-block-start"] = m["settings"]["padding-block-end"] = 12
for blk in m["blocks"].values():
    blk["settings"].update({"font": "var(--font-body--family)", "font_size": "0.875rem", "letter_spacing": "loose"})
coll = S["collections"]
coll["blocks"]["title"]["blocks"]["eyebrow"] = text("<p>ONTDEK</p>", preset="h6", align="center", width="100%")
coll["blocks"]["title"]["block_order"] = ["eyebrow", "h"]
coll["blocks"]["title"]["blocks"]["h"]["settings"]["text"] = "<h2>Waar ben je naar op zoek?</h2>"
coll["blocks"]["static-collection-card"]["blocks"]["collection-card-image"]["settings"]["image_ratio"] = "square"
st = S["steps"]
st["blocks"]["eyebrow"] = text("<p>ONZE BELOFTE</p>", preset="h6", align="center", width="100%")
st["block_order"] = ["eyebrow"] + st["block_order"]
st["blocks"]["heading"]["settings"]["text"] = "<h2>Zorgeloos shoppen bij Lovaire</h2>"
st["settings"]["color_scheme"] = "scheme-4"
S["spotlight_head"]["settings"]["color_scheme"] = S["spotlight"]["settings"]["color_scheme"] = "scheme-5"
S["story"]["settings"]["color_scheme"] = "scheme-1"
S["trust"]["blocks"]["usp"]["settings"]["icon_color"] = "#8b6b4a"
walk(idx); save("templates__index.json", idx)

for n in ["templates__product.json", "templates__collection.json", "templates__list-collections.json",
          "templates__page.json", "templates__page.contact.json", "sections__footer-group.json", "sections__header-group.json"]:
    d = load(n); walk(d)
    if n == "templates__product.json":
        d["sections"]["usps"]["blocks"]["usp"]["settings"]["icon_color"] = "#8b6b4a"
    if n in ("templates__collection.json", "templates__list-collections.json"):
        for s in d["sections"].values():
            if s.get("type") == "_blocks": s["blocks"]["usp"]["settings"]["icon_color"] = "#8b6b4a"
    save(n, d)
print("ok", idx["order"])

# --- Lyvelle-opbouw: hero → voordelen → favorieten → categorie-rondjes → belofte → verhaal → reviews → FAQ
idx = load("templates__index.json")
S = idx["sections"]
S["favorieten"] = {"type": "lovaire-favorieten", "settings": {
    "eyebrow": "ONZE FAVORIETEN", "heading": "Shop de Lovaire favorieten",
    "products": S["bestsellers"]["blocks"]["list"]["settings"]["selected_products"],
    "columns": 3, "button_label": "Shop alles →", "button_link": "shopify://collections/all",
    "background": "#ffffff", "padding_top": 64, "padding_bottom": 64}}
for k in ["bestsellers", "marquee", "spotlight_head", "spotlight"]:
    S.pop(k, None)
card = S["collections"]["blocks"]["static-collection-card"]
card["settings"]["border_radius"] = 0
card["blocks"]["collection-card-image"]["settings"].update({"image_ratio": "square", "border_radius": 100})
card["blocks"]["ctitle"]["settings"]["type_preset"] = "h5"
S["collections"]["settings"]["color_scheme"] = "scheme-1"
S["trust"]["settings"]["padding-block-start"] = S["trust"]["settings"]["padding-block-end"] = 8
idx["order"] = ["hero", "trust", "favorieten", "collections", "steps", "story", "reviews", "faq"]
save("templates__index.json", idx)
print("lyvelle-opbouw", idx["order"])
