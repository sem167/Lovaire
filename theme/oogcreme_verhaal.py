"""Oogcrème-pagina opgebouwd zoals lovelia.dk: na de video's een reeks verhaalblokken (vette kop, korte
gecentreerde tekst, foto over de volle breedte), daarna FAQ en koopblok. Eigen, eerlijke teksten."""
import json
F = "templates__product.oogcreme.json"
t = json.load(open(F))
S = t["sections"]
def blok(heading, text, image="", caption="", top=40, bottom=0, placeholder=False):
    return {"type": "lovaire-tekst-foto", "settings": {"heading": heading, "text": text, "image": image,
            "caption": caption, "full_bleed": True, "show_placeholder": placeholder, "background": "#ffffff",
            "padding_top": top, "padding_bottom": bottom}}
S.pop("voor_na", None)
S["moe"] = blok("Zie je er moe uit, ook als je goed hebt geslapen?",
  "<p>Je slaapt genoeg. Je drinkt water.</p>"
  "<p>En toch laten donkere kringen je er <strong>vermoeider uitzien dan je je voelt</strong>.</p>"
  "<p>De huid rond je ogen is dun en gevoelig. Daardoor vallen schaduwen en verkleuring sneller op.</p>"
  "<p>De <strong>Calcium Dark Spot Oogcrème</strong> geeft je een <strong>direct frissere blik</strong> – en verzorgt ondertussen je huid.</p>",
  "shopify://shop_images/6-voor-direct.jpg", "Illustratie – resultaten kunnen per persoon verschillen.", top=24)
S["waarom"] = blok("Waarom een gewone oogcrème vaak niet genoeg is",
  "<p>De meeste oogcrèmes <strong>verzorgen wel</strong>, maar je ziet in de spiegel niet meteen verschil.</p>"
  "<p>Een concealer camoufleert wel, maar <strong>verzorgt je huid niet</strong> en kan in fijne lijntjes kruipen.</p>"
  "<p>Daarom zoeken zoveel vrouwen naar <strong>één product dat allebei doet</strong>.</p>",
  "shopify://shop_images/3-textuur-swatch.jpg")
S["anders"] = blok("Wat deze oogcrème anders maakt",
  "<p>Deze Koreaanse oogcrème combineert <strong>directe camouflage</strong> met <strong>dagelijkse verzorging</strong>.</p>"
  "<p>• De lichte, beige getinte formule laat je huid <strong>meteen egaler en frisser</strong> ogen</p>"
  "<p>• <strong>Calcium, niacinamide en collageen</strong> verzorgen de dunne huid rond je ogen</p>"
  "<p>• Licht en romig, <strong>kruipt niet in fijne lijntjes</strong></p>"
  "<p>Eén potje. Eén stap. Een frisse blik.</p>",
  "shopify://shop_images/1-oogcreme-packshot.jpg")
S["gebruik"] = blok("Zo gebruik je het",
  "<p><strong>1.</strong> Gebruik het als laatste stap van je huidverzorging.</p>"
  "<p><strong>2.</strong> Breng een klein beetje aan onder beide ogen.</p>"
  "<p><strong>3.</strong> Strijk 2 à 4 keer zacht uit en klop licht in met je ringvinger.</p>",
  placeholder=True)
S["slot"] = blok("Zie er weer uit zoals je je voelt",
  "<p>Donkere kringen hoeven niet te bepalen hoe jij je voelt.</p>"
  "<p>Met de <strong>Calcium Dark Spot Oogcrème</strong> kies je voor een frisse, verzorgde blik – licht genoeg voor elke dag.</p>"
  "<p><strong>Ontdek je frissere blik vandaag nog.</strong></p>", bottom=48)
for k in ("benefits", "story", "compare", "howto", "belofte"):
    S.pop(k, None)
t["sections"]["videos"]["settings"]["padding_bottom"] = 8
t["order"] = ["main", "videos", "moe", "waarom", "anders", "gebruik", "slot", "faq", "cta"]
t["sections"]["faq"]["settings"]["blend_top"] = "#ffffff"
json.dump(t, open(F, "w"), ensure_ascii=False, indent=2)
print(t["order"])
