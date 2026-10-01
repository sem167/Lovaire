"""Collectie-, collectieoverzicht-, pagina- en contactsjablonen voor 'Lovaire – Nieuw design'."""
import json
from build import text, button, ordered, sec_flex, index

H = dict(font="var(--font-heading--family)", color="var(--color-foreground-heading)")
usps = {"type": "_blocks", "name": "Voordelen", "blocks": index["sections"]["trust"]["blocks"], "block_order": ["usp"],
        "settings": {**sec_flex, "color_scheme": "scheme-1", "padding-block-start": 16, "padding-block-end": 16}}

help_cta = {"type": "section", "name": "Hulp nodig", **ordered([
    ("h", text("<h2>Nog vragen? Wij helpen je graag</h2>", preset="h3", align="center", **H)),
    ("p", text("<p>Ons team reageert op werkdagen tussen 09:00 en 17:00.</p>", align="center")),
    ("b", button("Neem contact op", "shopify://pages/contact", "button-secondary")),
]), "settings": {**sec_flex, "gap": 16, "color_scheme": "scheme-5", "padding-block-start": 56, "padding-block-end": 56}}

product_card = {"type": "_product-card", "static": True, "settings": {"product_card_gap": 10, "inherit_color_scheme": True},
                "blocks": {
                    "card-gallery": {"type": "_product-card-gallery", "settings": {"image_ratio": "portrait", "border_radius": 20}, "blocks": {}},
                    "group": {"type": "_product-card-group", "settings": {"content_direction": "column", "gap": 4,
                                                                         "horizontal_alignment_flex_direction_column": "flex-start",
                                                                         "width": "fill", "width_mobile": "fill", "inherit_color_scheme": True},
                              **ordered([("title", {"type": "product-title", "settings": {"type_preset": "h5", "alignment": "left",
                                                                                          "color": "var(--color-foreground-heading)"}, "blocks": {}}),
                                         ("price", {"type": "price", "settings": {"show_sale_price_first": True, "type_preset": "paragraph",
                                                                                  "width": "100%", "alignment": "left"}, "blocks": {}})])}},
                "block_order": ["card-gallery", "group"]}

collection = {"sections": {
    "header": {"type": "section", "name": "Collectie-kop", **ordered([
        ("eyebrow", text("<p>LOVAIRE COLLECTIE</p>", preset="h6", align="center")),
        ("title", text("<h1>{{ closest.collection.title }}</h1>", preset="h1", align="center", **H)),
        ("desc", text("{{ closest.collection.description }}", align="center", max_width="narrow")),
    ]), "settings": {**sec_flex, "gap": 12, "color_scheme": "scheme-4", "padding-block-start": 56, "padding-block-end": 56}},
    "main": {"type": "main-collection", "blocks": {
        "filters": {"type": "filters", "static": True, "settings": {
            "enable_filtering": True, "filter_style": "horizontal", "filter_width": "centered",
            "enable_sorting": True, "enable_grid_density": True, "inherit_color_scheme": True}, "blocks": {}},
        "product-card": product_card},
        "settings": {"layout_type": "grid", "product_card_size": "medium", "mobile_product_card_size": "small",
                     "product_grid_width": "centered", "full_width_on_mobile": False,
                     "columns_gap_horizontal": 20, "columns_gap_vertical": 32,
                     "color_scheme": "scheme-1", "padding-block-start": 32, "padding-block-end": 56}},
    "usps": usps,
}, "order": ["header", "main", "usps"]}

list_collections = {"sections": {
    "main": {"type": "main-collection-list", "name": "Alle collecties", "blocks": {
        "head": {"type": "group", "settings": {"content_direction": "column", "gap": 8,
                                               "horizontal_alignment_flex_direction_column": "center",
                                               "width": "fill", "width_mobile": "fill", "inherit_color_scheme": True},
                 **ordered([("t", text("<h1>Alle collecties</h1>", preset="h1", align="center", width="100%", **H)),
                            ("p", text("<p>Ontdek onze beauty essentials per categorie.</p>", align="center", width="100%"))])},
        "static-collection-card": {"type": "_collection-card", "static": True, "settings": {
            "placement": "below_image", "horizontal_alignment": "center", "vertical_alignment": "flex-end",
            "collection_card_gap": 12, "inherit_color_scheme": True, "border": "none", "border_radius": 20},
            "blocks": {
                "collection-card-image": {"type": "_collection-card-image", "static": True,
                                          "settings": {"image_ratio": "portrait", "border": "none", "border_radius": 20}, "blocks": {}},
                "ctitle": {"type": "collection-title", "settings": {"alignment": "center", "type_preset": "h4",
                                                                    "color": "var(--color-foreground-heading)"}, "blocks": {}}},
            "block_order": ["ctitle"]}},
        "block_order": ["head"],
        "settings": {"layout_type": "grid", "carousel_on_mobile": False, "columns": 3, "mobile_columns": "2",
                     "columns_gap": 20, "rows_gap": 28, "max_collections": 12, "section_width": "page-width",
                     "gap": 32, "color_scheme": "scheme-1", "padding-block-start": 56, "padding-block-end": 56}},
    "usps": usps,
}, "order": ["main", "usps"]}

page = {"sections": {
    "main": {"type": "main-page", **ordered([
        ("heading", text("<h1>{{ closest.page.title }}</h1>", preset="h1", align="center", width="100%", **H)),
        ("page-content", {"type": "page-content", "settings": {}, "blocks": {}}),
    ]), "settings": {"gap": 40, "color_scheme": "scheme-1", "padding-block-start": 56, "padding-block-end": 72}},
    "help": help_cta,
}, "order": ["main", "help"]}

contact = {"sections": {
    "main": {"type": "main-page", **ordered([
        ("eyebrow", text("<p>KLANTENSERVICE</p>", preset="h6", align="center", width="100%")),
        ("title", text("<h1>Hoe kunnen we je helpen?</h1>", preset="h1", align="center", width="100%", **H)),
        ("content", text("{{ closest.page.content }}", align="center", width="100%")),
    ]), "settings": {"content_direction": "column", "gap": 16, "color_scheme": "scheme-4",
                     "padding-block-start": 56, "padding-block-end": 56}},
    "info": {"type": "section", "name": "Contactgegevens", **ordered([
        ("row", {"type": "group", "settings": {"content_direction": "row", "vertical_on_mobile": True, "gap": 24,
                                               "width": "fill", "width_mobile": "fill", "inherit_color_scheme": True},
                 **ordered([
                     ("c1", {"type": "group", "settings": {"content_direction": "column", "gap": 6, "width": "fill", "width_mobile": "fill",
                                                           "horizontal_alignment_flex_direction_column": "center", "inherit_color_scheme": True},
                             **ordered([("t", text("<h3>E-mail</h3>", preset="h4", align="center")),
                                        ("b", text("<p>lovairesupport@gmail.com</p>", align="center"))])}),
                     ("c2", {"type": "group", "settings": {"content_direction": "column", "gap": 6, "width": "fill", "width_mobile": "fill",
                                                           "horizontal_alignment_flex_direction_column": "center", "inherit_color_scheme": True},
                             **ordered([("t", text("<h3>Openingstijden</h3>", preset="h4", align="center")),
                                        ("b", text("<p>Ma–vr: 09:00–17:00<br/>Za: 10:00–14:00<br/>Zo: gesloten</p>", align="center"))])}),
                     ("c3", {"type": "group", "settings": {"content_direction": "column", "gap": 6, "width": "fill", "width_mobile": "fill",
                                                           "horizontal_alignment_flex_direction_column": "center", "inherit_color_scheme": True},
                             **ordered([("t", text("<h3>Bestelling volgen</h3>", preset="h4", align="center")),
                                        ("b", text("<p>Gebruik de track &amp; trace-link in je verzendmail.</p>", align="center"))])}),
                 ])}),
    ]), "settings": {**sec_flex, "gap": 24, "color_scheme": "scheme-1", "padding-block-start": 48, "padding-block-end": 24}},
    "form": {"type": "section", "name": "Contactformulier", **ordered([
        ("h", text("<h2>Stuur ons een bericht</h2>", preset="h3", align="center", **H)),
        ("form", {"type": "contact-form", "settings": {"width": "custom", "custom_width": 60, "width_mobile": "custom",
                                                       "custom_width_mobile": 100, "inherit_color_scheme": True},
                  "blocks": {"submit-button": {"type": "contact-form-submit-button", "static": True, "settings": {
                      "label": "Verstuur bericht", "style_class": "button", "width": "fit-content", "width_mobile": "fill"}, "blocks": {}}},
                  "block_order": []}),
    ]), "settings": {**sec_flex, "gap": 24, "color_scheme": "scheme-1", "padding-block-start": 24, "padding-block-end": 72}},
}, "order": ["main", "info", "form"]}

out = {"templates/collection.json": collection, "templates/list-collections.json": list_collections,
       "templates/page.json": page, "templates/page.contact.json": contact}
for k, v in out.items():
    json.dump(v, open(k.replace("/", "__"), "w"), ensure_ascii=False, indent=2)
json.dump({"themeId": "gid://shopify/OnlineStoreTheme/208207184211",
           "files": [{"filename": k, "body": {"type": "TEXT", "value": json.dumps(v, ensure_ascii=False, separators=(",", ":"))}}
                     for k, v in out.items()]}, open("upsert_pages.json", "w"), ensure_ascii=False)
print({k: len(json.dumps(v)) for k, v in out.items()})
