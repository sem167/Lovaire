"""Productpagina Tarte Dab & Go Uitgroei Concealer (zelfde opbouw als product.oogcreme / product.glow-palette).
Schrijft templates__product.uitgroei-concealer.json."""
import json

def acc_row(heading, html):
    k = heading[:4].lower()
    return {"type": "_accordion-row", "settings": {"heading": heading, "open_by_default": False, "icon": "none"},
            "blocks": {k + "_t": {"type": "text", "settings": {"text": html, "width": "100%", "max_width": "normal",
                "alignment": "left", "type_preset": "rte", "font": "var(--font-body--family)",
                "color": "var(--color-foreground)", "wrap": "pretty"}, "blocks": {}}},
            "block_order": [k + "_t"]}

def story(heading, text, image=None, top=40, bottom=0):
    s = {"heading": heading, "text": text, "full_bleed": True, "show_placeholder": False,
         "background": "#ffffff", "padding_top": top, "padding_bottom": bottom}
    if image:
        s["image"] = "shopify://shop_images/" + image
    return {"type": "lovaire-tekst-foto", "settings": s}

main = {
  "type": "product-information",
  "blocks": {
    "media-gallery": {"type": "_product-media-gallery", "static": True, "settings": {
      "media_presentation": "carousel", "media_columns": "one", "image_gap": 8, "icons_style": "arrow",
      "slideshow_controls_style": "thumbnails", "slideshow_mobile_controls_style": "dots",
      "thumbnail_position": "bottom", "thumbnail_width": 64, "thumbnail_radius": 10, "aspect_ratio": "adapt",
      "media_fit": "cover", "media_radius": 20, "zoom": True, "hide_variants": False}, "blocks": {}},
    "product-details": {"type": "_product-details", "static": True, "settings": {
      "width": "fill", "width_mobile": "fill", "height": "fit", "details_position": "flex-start", "gap": 18,
      "sticky_details_desktop": True, "inherit_color_scheme": True, "padding-block-start": 16,
      "padding-block-end": 0, "padding-inline-start": 12, "padding-inline-end": 12},
      "blocks": {
        "title": {"type": "text", "settings": {"text": "<h1>{{ closest.product.title }}</h1>", "width": "fit-content",
          "max_width": "normal", "alignment": "left", "type_preset": "h2", "font": "var(--font-heading--family)",
          "color": "var(--color-foreground-heading)", "wrap": "pretty"}, "blocks": {}},
        "price": {"type": "price", "settings": {"show_sale_price_first": True, "show_installments": True,
          "show_tax_info": False, "type_preset": "h4", "width": "100%", "alignment": "left"}, "blocks": {}},
        "variants": {"type": "variant-picker", "settings": {"variant_style": "buttons", "show_swatches": True,
          "alignment": "left", "padding-block-start": 4, "padding-block-end": 4}, "blocks": {}},
        "buy": {"type": "buy-buttons", "settings": {"stacking": True, "show_pickup_availability": False, "gift_card_form": True},
          "blocks": {"quantity": {"type": "quantity", "static": True, "settings": {}, "blocks": {}},
                     "add-to-cart": {"type": "add-to-cart", "static": True, "settings": {"style_class": "button"}, "blocks": {}},
                     "accelerated-checkout": {"type": "accelerated-checkout", "static": True, "settings": {}, "blocks": {}}},
          "block_order": []},
        "description": {"type": "product-description", "settings": {}, "blocks": {}},
        "info": {"type": "accordion", "settings": {"icon": "plus", "dividers": True, "type_preset": "h6", "inherit_color_scheme": True},
          "blocks": {
            "ship": acc_row("Verzending & levering", "<p>Je ontvangt een e-mail met een track-and-trace-link zodra je bestelling onderweg is. Meer info: <a href=\"/pages/verzendbeleid\">verzendbeleid</a>.</p>"),
            "ret": acc_row("Retourneren", "<p>Je kunt ongeopende producten binnen 30 dagen na ontvangst retourneren. Voor hygiëneproducten zoals cosmetica en ondergoed gelden aparte voorwaarden: zie <a href=\"/pages/ruilen-en-retourneren\">hygiëneproducten</a>. Alle stappen vind je op onze pagina <a href=\"/pages/bestellingen-en-levering-1\">ruilen en retourneren</a>.</p>"),
            "pay": acc_row("Veilig betalen", "<p>Je betaalt via de beveiligde checkout van Shopify, onder andere met iDEAL en Klarna. Wij zien of bewaren je betaalgegevens nooit.</p>"),
            "help": acc_row("Vragen? We helpen je graag", "<p>Mail ons via onze <a href=\"/pages/contact\">contactpagina</a>. Onze Nederlandse klantenservice is 24/7 voor je bereikbaar.</p>")},
          "block_order": ["ship", "ret", "pay", "help"]},
        "lovaire_trust": {"type": "lovaire-product-trust", "settings": {}, "blocks": {}},
        "lyvelle_intro": {"type": "lovaire-pdp-intro", "settings": {
          "subtitle": "Uitgroei en grijze haartjes weg in 5 seconden – waterproof",
          "pill_1_emoji": "⏱️", "pill_1_text": "Uitgroei gecamoufleerd in 5 seconden",
          "pill_2_emoji": "💧", "pill_2_text": "Waterproof, zonder plakkerig spraygevoel",
          "pill_3_emoji": "✨", "pill_3_text": "Ingebouwd sponsje – precies en zonder knoeien",
          "restyle_section": True, "button_color": "#6ab04c", "button_hover_color": "#5c9d40"}, "blocks": {}}},
      "block_order": ["title", "lyvelle_intro", "price", "variants", "buy", "lovaire_trust", "description", "info"]}},
  "settings": {"content_width": "content-center-aligned", "desktop_media_position": "left", "equal_columns": True,
    "limit_details_width": True, "gap": 48, "enable_sticky_add_to_cart": False, "color_scheme": "scheme-1",
    "padding-block-start": 32, "padding-block-end": 0}}

sections = {
  "main": main,
  "videos": {"type": "lovaire-video-duo", "settings": {"heading": "Zie de Dab & Go zelf in actie 💕",
    "background": "#ffffff", "padding_top": 8, "padding_bottom": 8}},
  "moe": story("Je uitgroei is er weer – en je kapper pas over weken?",
    "<p>Je kleur zit net mooi. En dan zie je ze toch weer: <strong>grijze haartjes en uitgroei</strong> bij je scheiding.</p>"
    "<p>Een nieuwe kleurbehandeling is nog lang niet aan de beurt. En een spray? Die plakt en komt overal behalve waar je hem wilt.</p>"
    "<p>Met de <strong>Dab & Go Uitgroei Concealer</strong> dep je je uitgroei in <strong>5 seconden</strong> weg.</p>",
    "dab-go-2-model.jpg", top=24),
  "waarom": story("Uitgroei, grijs en dunne plekjes – in één keer weg",
    "<p>• <strong>Grijze haartjes</strong> – direct gecamoufleerd</p>"
    "<p>• <strong>Uitgroei en uitgegroeide highlights</strong> – je kleur ziet er weer egaal uit</p>"
    "<p>• <strong>Scheiding en haarlijn</strong> – minder zichtbare hoofdhuid, voller ogend haar</p>"
    "<p>Zonder verf, zonder salon, zonder handigheid met haar.</p>",
    "dab-go-3-voor-na.jpg"),
  "anders": story("Wat deze concealer anders maakt",
    "<p>Het <strong>ingebouwde sponsje</strong> doet het werk voor je: je dept de kleur precies waar je hem nodig hebt.</p>"
    "<p>• <strong>Waterproof</strong> – zonder het plakkerige gevoel van een spray</p>"
    "<p>• <strong>Amazone-klei</strong> voor een betere, langere hechting</p>"
    "<p>• <strong>Argan-, druivenpit- en castorolie</strong> verzorgen je haar en maken het glad</p>"
    "<p>Vegan, cruelty-free en dermatologisch getest.</p>",
    "dab-go-4-sponsje.jpg"),
  "tinten": story("Zeven tinten, voor elke haarkleur",
    "<p><strong>Koel blond</strong> – licht, honing- en goudblond haar</p>"
    "<p><strong>Blond</strong> – as- en donkerblond haar</p>"
    "<p><strong>Lichtbruin</strong> – donkerblond, licht kastanje en lichtbruin haar</p>"
    "<p><strong>Middenbruin</strong> – middenbruin, kastanje en karamel haar</p>"
    "<p><strong>Donkerbruin</strong> – kastanje en donkerbruin haar</p>"
    "<p><strong>Zwartbruin</strong> – diepbruin en zwart haar</p>"
    "<p><strong>Grijs</strong> – peper-en-zout, zilver en grijs haar</p>",
    "dab-go-5-ugc.jpg"),
  "gebruik": story("Zo gebruik je het",
    "<p><strong>1.</strong> Draai de dop eraf en druk het sponsje in het dopje om kleur op te nemen.</p>"
    "<p><strong>2.</strong> Dep het direct op droge uitgroei, grijze haartjes of dunne plekjes.</p>"
    "<p><strong>3.</strong> Werk van binnen naar buiten tot je de gewenste dekking hebt.</p>"
    "<p><strong>Pro-tip:</strong> dep langs je scheiding en haarlijn voor voller ogend haar.</p>",
    "dab-go-1-stick.jpg"),
  "slot": story("Elke dag een verse kleur",
    "<p>Tussen twee kappersafspraken, voor een feestje of gewoon voor jezelf: met de <strong>Dab & Go</strong> ziet je haar er altijd verzorgd uit.</p>"
    "<p><strong>Dep je uitgroei vandaag nog weg.</strong></p>",
    None, bottom=48),
  "faq": {"type": "lovaire-product-faq", "settings": {"background": "#ffffff", "blend_top": "#ffffff", "blend_bottom": "#f9f5f1"}},
  "cta": {"type": "lovaire-product-cta", "settings": {"eyebrow": "KLAAR VOOR EEN VERSE KLEUR", "blend_top": "#f9f5f1", "blend_bottom": "#f6e7de"}},
}

tpl = {"sections": sections, "order": ["main", "videos", "moe", "waarom", "anders", "tinten", "gebruik", "slot", "faq", "cta"]}
with open(__file__.replace("build_dabgo.py", "templates__product.uitgroei-concealer.json"), "w") as f:
    json.dump(tpl, f, ensure_ascii=False, indent=2)
print("ok")
