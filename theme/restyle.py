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

# --- Eigen hero met sfeerfoto (Pexels 11179593), animaties, zwevend label en draaiend embleem
idx = load("templates__index.json")
idx["sections"]["hero"] = {"type": "lovaire-hero", "settings": {
    "image": "shopify://shop_images/lovaire-hero-glow.jpg", "focal": "center 25%",
    "eyebrow": "Lovaire beauty",
    "title": "<p>Voel je mooi, <em>elke dag</em></p>",
    "text": "Make-up, huid- en haarverzorging die je echt gebruikt. Zorgvuldig geselecteerd en altijd gratis verzonden.",
    "button_label": "Shop nu", "button_link": "shopify://collections/all",
    "button2_label": "Ontdek collecties", "button2_link": "/collections",
    "trust_1": "Gratis verzending", "trust_2": "Veilig betalen met iDEAL", "trust_3": "Persoonlijke service",
    "badge_title": "Altijd gratis verzending", "badge_text": "Met track & trace in je mail",
    "seal_text": "LOVAIRE · BEAUTY · ESSENTIALS · ",
    "background": "#f6e7de", "height": 85}}
save("templates__index.json", idx)
print("hero vervangen")

# --- Reviews: alleen echte Loox-reviews (letterlijk), met productlink en echt gemiddelde
idx = load("templates__index.json")
S = idx["sections"]
S["reviews"] = {"type": "lovaire-reviews", "blocks": {
    "tiffany": {"type": "review", "settings": {
        "text": "Ongelofelijk wat dit product doet. Ik ben 50 plus, door dit product zie je mijn rimpels oprecht minder. Heel natuurlijk en de kleur past zich inderdaad aan je eigen huidskleur. Heel erg tevreden.",
        "name": "Tiffany T.", "rating": 5, "product": "zelfkleurende-foundation-spf15"}}},
    "block_order": ["tiffany"],
    "settings": {"eyebrow": "ECHTE REVIEWS", "heading": "Wat klanten zeggen",
        "products": ["lashlift-waterproof-mascara", "zelfkleurende-foundation-spf15", "self-tanner-tanning-lotion",
                     "lovaire-hairboost-shampoo", "elektrische-spray-massage-borstel-lovaire", "lovaire-support-bh"],
        "note": "Reviews worden na een bestelling verzameld via Loox en ongewijzigd getoond.",
        "background": "#f6e7de", "padding_top": 72, "padding_bottom": 72}}
# echte sterren op productkaarten (lovaire-favorieten leest Loox-metafields)
save("templates__index.json", idx)
print("reviews echt")

# --- Strakker: belofte-iconenkaarten (vervangt stappen + losse voordelenbalk), echte sterren op productpagina
idx = load("templates__index.json")
S = idx["sections"]
S["belofte"] = {"type": "lovaire-belofte", "blocks": {
    "b1": {"type": "item", "settings": {"icon": "truck", "title": "Gratis verzending", "text": "Op elke bestelling, zonder minimumbedrag."}},
    "b2": {"type": "item", "settings": {"icon": "lock", "title": "Veilig betalen", "text": "Met iDEAL, Klarna en meer via een beveiligde checkout."}},
    "b3": {"type": "item", "settings": {"icon": "package", "title": "Track & trace", "text": "Volg je pakketje vanaf het moment van verzending."}},
    "b4": {"type": "item", "settings": {"icon": "chat", "title": "Persoonlijke service", "text": "Ma–vr van 09:00 tot 17:00 staan we voor je klaar."}}},
    "block_order": ["b1", "b2", "b3", "b4"],
    "settings": {"eyebrow": "ONZE BELOFTE", "heading": "Zorgeloos shoppen bij Lovaire", "show_payment": True,
                 "background": "#f6e7de", "padding_top": 80, "padding_bottom": 80}}
for k in ["steps", "trust"]:
    S.pop(k, None)
S["favorieten"]["settings"].update({"padding_top": 80, "padding_bottom": 72})
S["collections"]["settings"].update({"padding-block-start": 24, "padding-block-end": 80})
S["story"]["settings"].update({"padding-block-start": 88, "padding-block-end": 88})
S["faq"]["settings"].update({"padding-block-start": 80, "padding-block-end": 80})
idx["order"] = ["hero", "favorieten", "collections", "belofte", "story", "reviews", "faq"]
save("templates__index.json", idx)

prod = load("templates__product.json")
det = prod["sections"]["main"]["blocks"]["product-details"]
det["blocks"]["rating"] = {"type": "lovaire-rating", "settings": {}, "blocks": {}}
bo = det["block_order"]
if "rating" not in bo: bo.insert(bo.index("title") + 1, "rating")
save("templates__product.json", prod)
print("strakker", idx["order"])

# --- Lyvelle-mobiel: compacte voordelen, gestippelde categorie-rondjes, carrousel, statement, momenten-tabs
idx = load("templates__index.json")
S = idx["sections"]
S["belofte"]["settings"].update({"layout": "list", "eyebrow": "", "heading": "", "show_payment": False,
                                 "background": "#ffffff", "padding_top": 0, "padding_bottom": 0})
S["categories"] = {"type": "lovaire-categories", "settings": {
    "eyebrow": "ONTDEK", "heading": "Waar ben je naar op zoek?",
    "collections": ["make-up", "huid-producten", "haarverzorging", "beauty-tools", "shapewear"],
    "background": "#ffffff", "padding_top": 64, "padding_bottom": 64}}
S["favorieten"]["settings"].update({"tab_label": "Alle producten", "button_label": "Bekijk alles",
    "heading": "Shop de favorieten", "background": "#f6e9e1", "padding_top": 72, "padding_bottom": 72})
S["statement"] = {"type": "lovaire-statement", "settings": {
    "eyebrow": "LOVAIRE", "text": "<p>Make-up, huid en haar. Voor elk moment van <em>jouw dag</em>.</p>",
    "show_line": True, "background": "#ffffff", "padding_top": 96, "padding_bottom": 72}}
S["momenten"] = {"type": "lovaire-momenten", "blocks": {
    "m1": {"type": "moment", "settings": {"label": "Ochtend", "icon": "sun", "intro": "Een frisse, stralende start van je dag.",
           "products": ["zelfkleurende-foundation-spf15", "lashlift-waterproof-mascara"]}},
    "m2": {"type": "moment", "settings": {"label": "Overdag", "icon": "cloud", "intro": "Comfortabel en verzorgd de hele dag door.",
           "products": ["lovaire-support-bh", "self-tanner-tanning-lotion"]}},
    "m3": {"type": "moment", "settings": {"label": "Avond", "icon": "moon", "intro": "Even tijd voor jezelf.",
           "products": ["lovaire-hairboost-shampoo", "elektrische-spray-massage-borstel-lovaire"]}}},
    "block_order": ["m1", "m2", "m3"],
    "settings": {"eyebrow": "ELK MOMENT", "heading": "Jouw dag met Lovaire", "background": "#ffffff",
                 "padding_top": 24, "padding_bottom": 88}}
for k in ["collections", "story"]:
    S.pop(k, None)
idx["order"] = ["hero", "belofte", "categories", "favorieten", "statement", "momenten", "reviews", "faq"]
save("templates__index.json", idx)
print("lyvelle-mobiel", idx["order"])

# --- Collectiepagina's: categorie-rondjes als navigatie, strakke vierkante kaarten, compacte belofte
COLL = ["make-up", "huid-producten", "haarverzorging", "beauty-tools", "shapewear"]
def belofte_list(pad_top=0, pad_bottom=0, payment=True):
    b = json.loads(json.dumps(load("templates__index.json")["sections"]["belofte"]))
    b["settings"].update({"layout": "list", "eyebrow": "", "heading": "", "show_payment": payment,
                          "background": "#ffffff", "padding_top": pad_top, "padding_bottom": pad_bottom})
    return b
col = load("templates__collection.json")
C = col["sections"]
C["header"]["settings"].update({"color_scheme": "scheme-5", "padding-block-start": 48, "padding-block-end": 8})
C["nav"] = {"type": "lovaire-categories", "settings": {"eyebrow": "", "heading": "", "collections": COLL,
            "background": "#f6e7de", "padding_top": 16, "padding_bottom": 40}}
card = C["main"]["blocks"]["product-card"]["blocks"]
card["card-gallery"]["settings"].update({"image_ratio": "square", "border_radius": 0})
card["group"]["blocks"]["title"]["settings"]["type_preset"] = "h5"
C.pop("usps", None)
C["belofte"] = belofte_list(0, 40)
col["order"] = ["header", "nav", "main", "belofte"]
save("templates__collection.json", col)

lc = load("templates__list-collections.json")
lc["sections"] = {
    "intro": {"type": "lovaire-categories", "settings": {"eyebrow": "ONTDEK", "heading": "Alle collecties", "collections": COLL,
              "background": "#f6e7de", "padding_top": 64, "padding_bottom": 64}},
    "favorieten": json.loads(json.dumps(load("templates__index.json")["sections"]["favorieten"])),
    "belofte": belofte_list(0, 40)}
lc["sections"]["favorieten"]["settings"].update({"background": "#ffffff", "eyebrow": "ONZE FAVORIETEN", "heading": "Populair bij Lovaire"})
lc["order"] = ["intro", "favorieten", "belofte"]
save("templates__list-collections.json", lc)
print("collecties strak")
