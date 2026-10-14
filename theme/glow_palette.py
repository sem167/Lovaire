"""Productpagina Glow Palette: exact dezelfde opbouw als de oogcrème-pagina (templates/product.oogcreme.json)."""
import json
t = json.load(open("templates__product.oogcreme.json"))
s = t["sections"]
intro = s["main"]["blocks"]["product-details"]["blocks"]["lyvelle_intro"]["settings"]
intro.update({
    "subtitle": "Highlighter, oogschaduw én blush in één palette – voor een stralende glow",
    "pill_1_emoji": "✨", "pill_1_text": "4 tinten voor ogen & wangen",
    "pill_2_emoji": "🌅", "pill_2_text": "Golden-hour glow in een paar tellen",
    "pill_3_emoji": "👜", "pill_3_text": "Compact – past in elke tas",
})
s["videos"]["settings"].update({"heading": "Zie de Glow Palette zelf in actie ✨", "video_1": "", "video_2": ""})
for k in ("video_1", "video_2"):
    s["videos"]["settings"].pop(k)

def story(key, heading, text, pt=40, pb=0):
    st = s[key]["settings"]
    st.pop("image", None)
    st.update({"heading": heading, "text": text, "show_placeholder": key != "slot", "padding_top": pt, "padding_bottom": pb})

story("moe", "Wil je die glow, zonder tien producten?",
      "<p>Je ziet het overal: die frisse, stralende <strong>golden-hour glow</strong>.</p>"
      "<p>Maar met een losse highlighter, blush én oogschaduw raakt je make-uptasje snel vol – en duurt je ochtend lang.</p>"
      "<p>De <strong>Glow Palette</strong> geeft je alles in <strong>één compact palette</strong>.</p>", pt=24)
story("waarom", "Vier tinten, eindeloos veel looks",
      "<p>• <strong>Parel</strong> – een frisse highlight op je jukbeenderen en in je ooghoekjes</p>"
      "<p>• <strong>Goud</strong> – warme golden-hour glow op wangen en oogleden</p>"
      "<p>• <strong>Brons-rosé</strong> – zachte diepte op je ogen</p>"
      "<p>• <strong>Roze</strong> – een blosje met glans op je wangen</p>"
      "<p>Draag ze los of <strong>meng ze tot jouw eigen glow</strong>.</p>")
story("anders", "Wat deze palette anders maakt",
      "<p>Fijn poeder dat <strong>soepel uitblendt</strong> op je huid.</p>"
      "<p>• <strong>Voor ogen én wangen</strong> – één palette in plaats van drie producten</p>"
      "<p>• <strong>Opbouwbaar</strong> – van subtiel overdag tot stralend in de avond</p>"
      "<p>• <strong>Compact</strong> – ideaal voor onderweg of op reis</p>"
      "<p>Eén palette. Een paar tellen. Jouw glow.</p>")
story("gebruik", "Zo gebruik je het",
      "<p><strong>1.</strong> Draai je kwast door één tint, of door de hele palette voor een mix.</p>"
      "<p><strong>2.</strong> Dep op je jukbeenderen, wenkbrauwboog, oogleden en binnenste ooghoek.</p>"
      "<p><strong>3.</strong> Bouw laagje voor laagje op tot de glow die jij wilt.</p>")
story("slot", "Glow zoals jij dat wilt",
      "<p>Een natuurlijke dagglow of een stralende avondlook – met de <strong>Glow Palette</strong> heb je het allemaal in één hand.</p>"
      "<p><strong>Ontdek jouw glow vandaag nog.</strong></p>", pb=48)
s["cta"]["settings"]["eyebrow"] = "KLAAR VOOR JOUW GLOW"
json.dump(t, open("templates__product.glow-palette.json", "w"), ensure_ascii=False, indent=2)
print(t["order"])

# Foto's (aangeleverd door de gebruiker) in de verhaalblokken
t = json.load(open("templates__product.glow-palette.json"))
for key, img in {"moe": "glow-palette-all-in-1.jpg", "waarom": "glow-palette-tinten.jpg",
                 "anders": "glow-palette-glow-your-way.jpg", "gebruik": "glow-palette-zo-aanbrengen.jpg"}.items():
    t["sections"][key]["settings"]["image"] = "shopify://shop_images/" + img
    t["sections"][key]["settings"]["show_placeholder"] = False
json.dump(t, open("templates__product.glow-palette.json", "w"), ensure_ascii=False, indent=2)
