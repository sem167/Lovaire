"""Homepage in Meroda-stijl (templates/index.json) + aangepaste aankondigingsbalk (sections/header-group.json).
Leest de huidige index.json/header-group.json uit /tmp-pad van argv en schrijft templates__index.json en sections__header-group.json."""
import json, re, sys

def load(path):
    s = open(path).read()
    s = re.sub(r'^/\*.*?\*/\s*', '', s, flags=re.S)
    return json.loads(s)

cur = load(sys.argv[1])
hdr = load(sys.argv[2])
img = lambda f: "shopify://shop_images/" + f

sections = {
  "trust": {"type": "lovaire-m-trust",
    "blocks": {"t1": {"type": "item", "settings": {"text": "30 dagen retourrecht"}},
               "t2": {"type": "item", "settings": {"text": "Altijd gratis verzending"}},
               "t3": {"type": "item", "settings": {"text": "Veilig betalen met iDEAL & Klarna"}}},
    "block_order": ["t1", "t2", "t3"],
    "settings": {"speed": 4, "background": "#f8f6f3", "text_color": "#1f1f1f", "border": "#e7e2dc"}},
  "hero": {"type": "lovaire-m-hero", "settings": {
    "title_top": "De glow van het seizoen", "title_accent": "Tarte Glow Palette",
    "text": "Oogschaduw én highlighter in één palette. Nu 1+1 gratis.",
    "button_label": "Shop de Glow Palette", "button_link": "shopify://products/glow-palette-highlighter-ogen-wangen",
    "image": img("glow-palette-all-in-1.jpg"), "focal": "center center", "desktop_height": 80,
    "serif_font": "playfair_display_i4", "bg_top": "#3d1f24", "bg_bottom": "#6e3b41",
    "text_color": "#ffffff", "button_bg": "#ffffff", "button_text": "#1f1f1f"}},
  "cats": {"type": "lovaire-m-categories",
    "blocks": {"c1": {"type": "category", "settings": {"image": img("glow-palette-glow-your-way.jpg"), "label": "Make-up", "link": "shopify://collections/make-up"}},
               "c2": {"type": "category", "settings": {"image": img("5-hero-helderdere-ogen.jpg"), "label": "Huidverzorging", "link": "shopify://collections/huid-producten"}},
               "c3": {"type": "category", "settings": {"image": img("dab-go-5-ugc.jpg"), "label": "Haar", "link": "shopify://collections/haarverzorging"}}},
    "block_order": ["c1", "c2", "c3"],
    "settings": {"heading": "Shop per categorie", "link_label": "Shop alles", "link": "shopify://collections/all",
                 "background": "#f8f6f3", "padding_top": 64, "padding_bottom": 40}},
  "loved": {"type": "lovaire-m-products",
    "blocks": {"p1": {"type": "product", "settings": {"product": "glow-palette-highlighter-ogen-wangen", "badge": "Bestseller"}},
               "p2": {"type": "product", "settings": {"product": "tarte-dab-go-uitgroei-concealer", "badge": "Nieuw", "options_label": "Kies je tint"}},
               "p3": {"type": "product", "settings": {"product": "dr-melaxin-calcium-dark-spot-cover-oogcreme-15g", "badge": "K-beauty"}},
               "p4": {"type": "product", "settings": {"product": "glow-kwast", "badge": ""}}},
    "block_order": ["p1", "p2", "p3", "p4"],
    "settings": {"heading": "Onze favorieten", "link_label": "Bekijk alles", "link": "shopify://collections/all",
                 "add_label": "In winkelwagen", "options_label": "Kies je tint",
                 "background": "#f8f6f3", "card_bg": "#f3ede6", "padding_top": 40, "padding_bottom": 56}},
  "feat_dabgo": {"type": "lovaire-m-feature", "settings": {
    "image": img("dab-go-2-model.jpg"), "focal": "center 30%", "eyebrow": "Nieuw bij Lovaire",
    "title": "Tarte Dab & Go Uitgroei Concealer", "text": "Uitgroei en grijze haartjes weg in 5 seconden. Waterproof, in zeven tinten.",
    "button_label": "Ontdek", "button_link": "shopify://products/tarte-dab-go-uitgroei-concealer",
    "image_right": False, "background": "#f8f6f3", "padding_top": 24, "padding_bottom": 56}},
  "feat_oog": {"type": "lovaire-m-feature", "settings": {
    "image": img("6-voor-direct.jpg"), "focal": "center center", "eyebrow": "Het K-beauty geheim",
    "title": "Calcium Dark Spot Oogcrème", "text": "Oogcrème én concealer in één: camoufleert donkere kringen direct en verzorgt de huid rond je ogen.",
    "button_label": "Ontdek", "button_link": "shopify://products/dr-melaxin-calcium-dark-spot-cover-oogcreme-15g",
    "image_right": True, "background": "#f8f6f3", "padding_top": 24, "padding_bottom": 56}},
  "gallery": {"type": "lovaire-m-gallery",
    "blocks": {"g1": {"type": "photo", "settings": {"image": img("glow-palette-ugc-1.jpg"), "product": "glow-palette-highlighter-ogen-wangen"}},
               "g2": {"type": "photo", "settings": {"image": img("glow-palette-ugc-4.jpg"), "product": "glow-palette-highlighter-ogen-wangen"}},
               "g3": {"type": "photo", "settings": {"image": img("oogcreme-oog-druppels.jpg"), "product": "dr-melaxin-calcium-dark-spot-cover-oogcreme-15g"}},
               "g4": {"type": "photo", "settings": {"image": img("glow-palette-ugc-6.jpg"), "product": "glow-palette-highlighter-ogen-wangen"}}},
    "block_order": ["g1", "g2", "g3", "g4"],
    "settings": {"heading": "#LovaireGlow", "subheading": "Zo dragen jullie het", "background": "#f8f6f3", "padding_top": 40, "padding_bottom": 64}},
}
# Bestaande blokken die blijven: de beloftelijst en de veelgestelde vragen
sections["belofte"] = cur["sections"]["belofte"]
sections["belofte"]["settings"].update({"background": "#f8f6f3", "padding_top": 8, "padding_bottom": 8, "blend_top": "#f8f6f3", "blend_bottom": "#f8f6f3"})
sections["faq"] = cur["sections"]["faq"]
sections["fade_end"] = {"type": "lovaire-fade", "settings": {"from": "#ffffff", "to": "#f6e7de", "height": 120}}

index = {"sections": sections,
         "order": ["trust", "hero", "cats", "loved", "feat_dabgo", "feat_oog", "gallery", "belofte", "faq", "fade_end"]}
open("templates__index.json", "w").write(json.dumps(index, ensure_ascii=False, indent=2))

ann = hdr["sections"]["header_announcements_pbXTDf"]
base = ann["blocks"]["a1"]["settings"]
ann["blocks"] = {"a1": {"type": "_announcement", "settings": dict(base, text="1+1 gratis op onze bestsellers · Gratis verzending", link="shopify://collections/all"), "blocks": {}}}
ann["block_order"] = ["a1"]
ann["settings"]["color_scheme"] = "scheme-4"
open("sections__header-group.json", "w").write(json.dumps(hdr, ensure_ascii=False, indent=2))
print("ok")
