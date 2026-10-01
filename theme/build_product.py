"""Universele, vertrouwenwekkende productpagina + homepage-uitbreiding voor 'Lovaire – Nieuw design'."""
import json
from build import text, button, ordered, faq_row, sec_flex, index, CREAM, BLUSH, NUDE, ROSE, COCOA, COCOA_TEXT, WHITE

TRUST_LINES = ("<p><strong>DE LOVAIRE BELOFTE</strong><br/>✓ Altijd gratis verzending<br/>"
               "✓ Veilig betalen met iDEAL of Klarna<br/>"
               "✓ Levertijd 5–12 werkdagen, met track &amp; trace</p>")

product = {"sections": {
    "main": {"type": "product-information", "blocks": {
        "media-gallery": {"type": "_product-media-gallery", "static": True, "settings": {
            "media_presentation": "carousel", "media_columns": "one", "image_gap": 8,
            "icons_style": "arrow", "slideshow_controls_style": "thumbnails",
            "slideshow_mobile_controls_style": "dots", "thumbnail_position": "bottom",
            "thumbnail_width": 64, "thumbnail_radius": 10, "aspect_ratio": "1/1.25",
            "media_fit": "cover", "media_radius": 20, "zoom": True, "hide_variants": False}, "blocks": {}},
        "product-details": {"type": "_product-details", "static": True, "settings": {
            "width": "fill", "width_mobile": "fill", "height": "fit", "details_position": "flex-start",
            "gap": 16, "sticky_details_desktop": True, "inherit_color_scheme": True,
            "padding-block-start": 16, "padding-block-end": 16,
            "padding-inline-start": 12, "padding-inline-end": 12},
            **ordered([
                ("vendor", text("<p>LOVAIRE</p>", preset="h6")),
                ("title", text("<h1>{{ closest.product.title }}</h1>", preset="h2",
                               font="var(--font-heading--family)", color="var(--color-foreground-heading)")),
                ("price", {"type": "price", "settings": {"show_sale_price_first": True, "show_installments": True,
                                                         "show_tax_info": True, "type_preset": "h4",
                                                         "width": "100%", "alignment": "left"}, "blocks": {}}),
                ("variants", {"type": "variant-picker", "settings": {"variant_style": "buttons", "show_swatches": True,
                                                                     "alignment": "left", "padding-block-start": 4,
                                                                     "padding-block-end": 4}, "blocks": {}}),
                ("buy", {"type": "buy-buttons", "settings": {"stacking": True, "show_pickup_availability": False,
                                                             "gift_card_form": True}, "blocks": {
                    "quantity": {"type": "quantity", "static": True, "settings": {}, "blocks": {}},
                    "add-to-cart": {"type": "add-to-cart", "static": True, "settings": {"style_class": "button"}, "blocks": {}},
                    "accelerated-checkout": {"type": "accelerated-checkout", "static": True, "settings": {}, "blocks": {}}},
                    "block_order": []}),
                ("payicons", {"type": "payment-icons", "settings": {"horizontal_alignment": "center", "gap": 8,
                                                                    "padding-block-start": 4, "padding-block-end": 4}, "blocks": {}}),
                ("trust", {"type": "text", "settings": {
                    "text": TRUST_LINES, "width": "100%", "alignment": "left", "type_preset": "rte",
                    "font": "var(--font-body--family)", "color": "var(--color-foreground)", "wrap": "pretty",
                    "background": True, "background_color": BLUSH, "corner_radius": 16,
                    "padding-block-start": 16, "padding-block-end": 16,
                    "padding-inline-start": 18, "padding-inline-end": 18}, "blocks": {}}),
                ("description", {"type": "product-description", "settings": {}, "blocks": {}}),
                ("info", {"type": "accordion", "settings": {"icon": "plus", "dividers": True, "type_preset": "h6",
                                                            "inherit_color_scheme": True}, **ordered([
                    faq_row("ship", "Verzending & levering",
                            "De gemiddelde levertijd is 5 tot 12 werkdagen. Je ontvangt een e-mail met track &amp; trace zodra je bestelling onderweg is. Meer info: <a href=\"/pages/verzendbeleid\">verzendbeleid</a>."),
                    faq_row("ret", "Retourneren",
                            "Je kunt je bestelling tot 14 dagen na ontvangst retourneren. Voor hygiënische producten, zoals cosmetica en ondergoed, gelden aparte voorwaarden: zie <a href=\"/pages/ruilen-en-retourneren\">hygiënische producten</a>. Alle stappen vind je op <a href=\"/pages/bestellingen-en-levering-1\">Ruilen en retourneren</a>."),
                    faq_row("pay", "Veilig betalen",
                            "Je betaalt via de beveiligde checkout van Shopify, met o.a. iDEAL en Klarna. Wij zien en bewaren nooit je betaalgegevens."),
                    faq_row("help", "Vragen? Wij helpen je graag",
                            "Mail ons via de <a href=\"/pages/contact\">contactpagina</a>. We reageren op werkdagen tussen 09:00 en 17:00."),
                ])}),
            ])}},
        "settings": {"content_width": "content-center-aligned", "desktop_media_position": "left",
                     "equal_columns": True, "limit_details_width": True, "gap": 48,
                     "enable_sticky_add_to_cart": True, "color_scheme": "scheme-1",
                     "padding-block-start": 32, "padding-block-end": 48}},

    "usps": {"type": "_blocks", "name": "Voordelen", "blocks": index["sections"]["trust"]["blocks"],
             "block_order": ["usp"],
             "settings": {**sec_flex, "color_scheme": "scheme-1", "padding-block-start": 0, "padding-block-end": 24}},

    "recommendations": {"type": "product-recommendations", "name": "Aanbevolen", "blocks": {
        "heading": text("<h2>Misschien vind je dit ook mooi</h2>", preset="h2",
                        font="var(--font-heading--family)", color="var(--color-foreground-heading)"),
        "static-product-card": {"type": "_product-card", "static": True, "settings": {
            "product_card_gap": 12, "inherit_color_scheme": True}, "blocks": {
            "gallery": {"type": "_product-card-gallery", "settings": {"image_ratio": "portrait", "border_radius": 20}, "blocks": {}},
            "group": {"type": "_product-card-group", "settings": {"content_direction": "column", "gap": 4,
                                                                 "horizontal_alignment_flex_direction_column": "flex-start",
                                                                 "width": "fill", "width_mobile": "fill", "inherit_color_scheme": True},
                      **ordered([("t", {"type": "product-title", "settings": {"type_preset": "h5", "alignment": "left",
                                                                                "color": "var(--color-foreground-heading)"}, "blocks": {}}),
                                 ("p", {"type": "price", "settings": {"show_sale_price_first": True, "type_preset": "paragraph",
                                                                      "width": "100%", "alignment": "left"}, "blocks": {}})])}},
            "block_order": ["gallery", "group"]}},
        "block_order": ["heading"],
        "settings": {"product": "{{ closest.product }}", "recommendation_type": "related", "layout_type": "grid",
                     "carousel_on_mobile": True, "max_products": 4, "columns": 4, "mobile_columns": "2",
                     "columns_gap": 16, "rows_gap": 24, "section_width": "page-width", "gap": 28,
                     "color_scheme": "scheme-5", "padding-block-start": 64, "padding-block-end": 64}},
}, "order": ["main", "usps", "recommendations"]}

# Homepage: "Zo werkt bestellen" na de collecties
def step(num, title, body):
    return {"type": "group", "settings": {"content_direction": "column", "gap": 8,
                                          "horizontal_alignment_flex_direction_column": "center",
                                          "width": "fill", "width_mobile": "fill", "inherit_color_scheme": True,
                                          "padding-block-start": 8, "padding-block-end": 8},
            **ordered([("n", text(f"<p>{num}</p>", preset="h2", align="center", font="var(--font-heading--family)",
                                  color="var(--color-primary)")),
                       ("t", text(f"<h3>{title}</h3>", preset="h4", align="center")),
                       ("b", text(f"<p>{body}</p>", align="center", max_width="narrow"))])}

index["sections"]["steps"] = {"type": "section", "name": "Zo werkt bestellen", **ordered([
    ("heading", text("<h2>Zorgeloos bestellen bij Lovaire</h2>", preset="h2", align="center", width="100%",
                     font="var(--font-heading--family)", color="var(--color-foreground-heading)")),
    ("row", {"type": "group", "settings": {"content_direction": "row", "vertical_on_mobile": True, "gap": 32,
                                           "width": "fill", "width_mobile": "fill", "inherit_color_scheme": True},
             **ordered([
                 ("s1", step("01", "Bestel veilig", "Betaal vertrouwd met iDEAL of Klarna via de beveiligde checkout.")),
                 ("s2", step("02", "Gratis verzonden", "Binnen 5–12 werkdagen bij je thuis, met track &amp; trace in je mail.")),
                 ("s3", step("03", "Persoonlijke hulp", "Een vraag of probleem? Mail ons, we reageren op werkdagen tussen 09:00 en 17:00.")),
             ])}),
]), "settings": {**sec_flex, "gap": 40, "color_scheme": "scheme-5",
                 "padding-block-start": 72, "padding-block-end": 72}}
order = index["order"]
order.insert(order.index("story"), "steps")

out = {"templates/product.json": product, "templates/index.json": index}
for name in ["product.support-bh-2", "product.tanning-oil", "product.foundation", "product.kam"]:
    out[f"templates/{name}.json"] = product

variables = {"themeId": "gid://shopify/OnlineStoreTheme/208207184211",
             "files": [{"filename": k, "body": {"type": "TEXT", "value": json.dumps(v, ensure_ascii=False, separators=(",", ":"))}}
                       for k, v in out.items()]}
json.dump(variables, open("upsert_product.json", "w"), ensure_ascii=False)
json.dump(product, open("templates__product.json", "w"), ensure_ascii=False, indent=2)
json.dump(index, open("templates__index.json", "w"), ensure_ascii=False, indent=2)
print(index["order"], len(json.dumps(variables)))

# --- Extra: bewegende tekstband, spotlight en warmere teksten ---
def marquee_text(t):
    return {"type": "text", "settings": {"text": f"<p>{t}</p>", "type_preset": "custom",
                                         "font": "var(--font-heading--family)", "font_size": "var(--font-size--h4)",
                                         "line_height": "tight", "letter_spacing": "loose", "case": "uppercase",
                                         "wrap": "nowrap", "width": "fit-content"}, "blocks": {}}

index["sections"]["marquee"] = {"type": "marquee", "name": "Bewegende tekst", **ordered([
    (f"m{i}", marquee_text(t)) for i, t in enumerate(
        ["Lovaire", "✦", "Jouw glow", "✦", "Selfcare", "✦", "Altijd gratis verzending", "✦", "Voel je mooi", "✦"])
]), "settings": {"movement_direction": "reverse", "color_scheme": "scheme-3",
                 "padding-block-start": 18, "padding-block-end": 18, "gap_between_elements": 28}}

index["sections"]["spotlight_head"] = {"type": "section", "name": "Spotlight-kop", **ordered([
    ("eyebrow", text("<p>LOVAIRE SPOTLIGHT</p>", preset="h6", align="center")),
    ("h", text("<h2>Wimpers die de hele dag blijven stralen</h2>", preset="h2", align="center", max_width="narrow",
               font="var(--font-heading--family)", color="var(--color-foreground-heading)")),
]), "settings": {**sec_flex, "gap": 12, "color_scheme": "scheme-4", "padding-block-start": 64, "padding-block-end": 24}}

index["sections"]["spotlight"] = {"type": "featured-product", "name": "Spotlight", "blocks": {
    "media": {"type": "_media-without-appearance", "static": True, "settings": {}, "blocks": {}},
    "featured-product": {"type": "_featured-product", "static": True, "settings": {}, "blocks": {
        "featured-product-title": {"type": "product-title", "static": True, "settings": {"type_preset": "h3", "width": "100%"}, "blocks": {}},
        "featured-product-price": {"type": "_featured-product-price", "static": True, "settings": {}, "blocks": {}},
        "featured-product-gallery": {"type": "_featured-product-gallery", "static": True, "settings": {}, "blocks": {}},
        "featured-product-swatches": {"type": "swatches", "static": True, "settings": {"hide_padding": True}, "blocks": {}}}}},
    "settings": {"product": "lashlift-waterproof-mascara", "layout": "media-left", "color_scheme": "scheme-4",
                 "padding-block-start": 0, "padding-block-end": 64}}

S = index["sections"]
S["bestsellers"]["blocks"]["list"]["settings"]["heading"] = "De Lovaire favorieten"
S["reviews"]["settings"]["heading"] = "<p>Waarom klanten van Lovaire houden</p>"
S["story"]["blocks"]["heading"]["settings"]["text"] = "<h2>Voor elke vrouw die zich mooi wil voelen</h2>"
S["story"]["blocks"]["body"]["settings"]["text"] = ("<p>Zie jij ook steeds die virale beautyproducten voorbijkomen op TikTok en Instagram? "
    "Bij Lovaire brengen we ze samen: zorgvuldig geselecteerde essentials voor je make-up, huid en haar. "
    "Zodat jij elke dag met een glimlach in de spiegel kijkt.</p>")
S["collections"]["blocks"]["title"]["blocks"]["h"]["settings"]["text"] = "<h2>Shop Lovaire</h2>"
index["order"] = ["hero", "marquee", "trust", "collections", "bestsellers", "steps", "spotlight_head", "spotlight",
                  "story", "reviews", "faq"]
json.dump(index, open("templates__index.json", "w"), ensure_ascii=False, indent=2)
