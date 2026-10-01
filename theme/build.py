"""Genereert het nieuwe Lovaire-design (zacht & vrouwelijk) voor het Dwell-thema."""
import json

# Palet
CREAM, BLUSH, NUDE, ROSE, SAND = "#f5f0e8", "#ede4d8", "#e6d9c7", "#111111", "#d8c8b4"
HOVER = "#3a3a3a"
COCOA, COCOA_TEXT, WHITE = "#111111", "#3a3a3a", "#ffffff"


def scheme(bg, heading, text, accent, btn_bg, btn_text, btn_hover_bg, border, sec_bg, sec_text):
    return {"settings": {
        "background": bg, "foreground_heading": heading, "foreground": text,
        "primary": accent, "primary_hover": heading, "border": border, "shadow": "#00000014",
        "primary_button_background": btn_bg, "primary_button_text": btn_text,
        "primary_button_border": btn_bg, "primary_button_hover_background": btn_hover_bg,
        "primary_button_hover_text": WHITE, "primary_button_hover_border": btn_hover_bg,
        "secondary_button_background": sec_bg, "secondary_button_text": sec_text,
        "secondary_button_border": sec_text, "secondary_button_hover_background": sec_text,
        "secondary_button_hover_text": WHITE if sec_text == COCOA else COCOA,
        "secondary_button_hover_border": sec_text,
        "input_background": WHITE, "input_text_color": COCOA, "input_border_color": border,
        "input_hover_background": CREAM,
        "variant_background_color": WHITE, "variant_text_color": COCOA,
        "variant_border_color": border, "variant_hover_background_color": BLUSH,
        "variant_hover_text_color": COCOA, "variant_hover_border_color": COCOA,
        "selected_variant_background_color": COCOA, "selected_variant_text_color": WHITE,
        "selected_variant_border_color": COCOA, "selected_variant_hover_background_color": HOVER,
        "selected_variant_hover_text_color": WHITE, "selected_variant_hover_border_color": HOVER,
    }}


T = "rgba(0,0,0,0)"
schemes = {
    # Basis: crème met cacao tekst
    "scheme-1": scheme(CREAM, COCOA, COCOA_TEXT, ROSE, COCOA, WHITE, HOVER, "#ddd2c3", T, COCOA),
    # Accent: oudroze (o.a. sale-badges)
    "scheme-2": scheme(ROSE, WHITE, WHITE, WHITE, WHITE, COCOA, COCOA, "#ffffff40", T, WHITE),
    # Donker: cacao (footer)
    "scheme-3": scheme(COCOA, CREAM, "#e9dfd1cc", NUDE, CREAM, COCOA, HOVER, "#ffffff26", T, CREAM),
    # Nude (verhaal / uitverkocht-badge)
    "scheme-4": scheme(NUDE, COCOA, COCOA_TEXT, ROSE, COCOA, WHITE, HOVER, "#11111120", T, COCOA),
    # Blush (nieuwsbrief, kaarten)
    "scheme-5": scheme(BLUSH, COCOA, COCOA_TEXT, ROSE, COCOA, WHITE, HOVER, "#11111120", T, COCOA),
    # Transparant met witte tekst (over foto's)
    "scheme-6": scheme(T, WHITE, WHITE, WHITE, WHITE, COCOA, ROSE, T, T, WHITE),
    # Transparant met donkere tekst
    "scheme-7": scheme(T, COCOA, COCOA_TEXT, ROSE, COCOA, WHITE, HOVER, "#ddd2c3", T, COCOA),
    "scheme-warm-beige": scheme(SAND, COCOA, COCOA_TEXT, COCOA, COCOA, WHITE, HOVER, "#11111126", T, COCOA),
    "scheme-announcement-black": scheme(COCOA, CREAM, CREAM, CREAM, CREAM, COCOA, HOVER, "#ffffff26", T, CREAM),
}

settings_data = {
    "current": {
        "logo": "shopify://shop_images/WhatsApp_Image_2026-09-14_at_11.41.14.jpg",
        "logo_height": 80, "logo_height_mobile": 64,
        "type_heading_font": "josefin_sans_n4",
        "type_subheading_font": "jost_n5",
        "type_body_font": "jost_n4",
        "type_accent_font": "jost_n5",
        "type_size_paragraph": "15",
        "type_size_h2": "40",
        "type_font_h3": "heading", "type_size_h3": "26",
        "type_font_h4": "accent", "type_size_h4": "15",
        "type_letter_spacing_h4": "heading-loose", "type_case_h4": "uppercase",
        "type_size_h5": "16",
        "type_font_h6": "accent", "type_size_h6": "12",
        "type_line_height_h6": "display-normal",
        "type_letter_spacing_h6": "heading-loose", "type_case_h6": "uppercase",
        "badge_corner_radius": 0,
        "badge_sale_color_scheme": "scheme-2",
        "badge_sold_out_color_scheme": "scheme-4",
        "badge_font_family": "accent", "badge_text_transform": "uppercase",
        "button_border_radius_primary": 0,
        "secondary_button_border_width": 1,
        "button_border_radius_secondary": 0,
        "cart_type": "page", "auto_open_cart_drawer": True,
        "inputs_border_radius": 0,
        "type_preset": "paragraph",
        "popover_border": "none",
        "currency_code_enabled_product_pages": False,
        "currency_code_enabled_product_cards": False,
        "variant_swatch_radius": 0, "variant_button_radius": 0,
        "variant_button_width": "default-width-buttons",
        "sections": {"password-footer": {"type": "password-footer", "settings": {"color_scheme": ""}}},
        "content_for_index": [],
        # App-embeds van de huidige winkel (Loox, Kaching, Upcart) blijven actief
        "blocks": {
            "11532412952436166569": {"type": "shopify://apps/loox-reviews/blocks/loox-inject/5c3b337f-fd14-4df5-b1d6-80ec13e6e28e", "disabled": False, "settings": {}},
            "15557474716127144420": {"type": "shopify://apps/kaching-bundles/blocks/app-embed-block/6c637362-a106-4a32-94ac-94dcfd68cdb8", "disabled": False, "settings": {}},
            "14952540001915115444": {"type": "shopify://apps/upcart-cart-drawer/blocks/app-embed/af3da5fb-f5f7-40ec-8273-41bf50059d4b", "disabled": False, "settings": {}},
        },
        "color_schemes": schemes,
    },
    }


def text(html, preset="rte", align="left", width="fit-content", max_width="normal", color="var(--color-foreground)", font="var(--font-body--family)"):
    return {"type": "text", "settings": {
        "text": html, "width": width, "max_width": max_width, "alignment": align,
        "type_preset": preset, "font": font, "color": color, "wrap": "pretty"}, "blocks": {}}


def button(label, link, style="button"):
    return {"type": "button", "settings": {"label": label, "link": link, "style_class": style,
                                           "width": "fit-content", "width_mobile": "fit-content"}, "blocks": {}}


def ordered(blocks):
    return {"blocks": dict(blocks), "block_order": [k for k, _ in blocks]}


def faq_row(key, q, a):
    return (key, {"type": "_accordion-row", "settings": {"heading": q, "open_by_default": False, "icon": "none"},
                  **ordered([(key + "_t", text(f"<p>{a}</p>", width="100%"))])})


sec_flex = {"content_direction": "column", "vertical_on_mobile": True,
            "horizontal_alignment_flex_direction_column": "center",
            "vertical_alignment_flex_direction_column": "center", "section_width": "page-width"}

index = {"sections": {
    "hero": {"type": "hero", "name": "Hero", **ordered([
        ("eyebrow", text("<p>LOVAIRE BEAUTY</p>", preset="h6", align="center", color="var(--color-foreground)")),
        ("heading", text("<h1>JOUW GLOW, ELKE DAG</h1>", preset="h1", align="center", font="var(--font-heading--family)", color="var(--color-foreground-heading)")),
        ("subtext", text("<p>Beauty essentials die jouw natuurlijke schoonheid laten stralen.</p>", align="center")),
        ("buttons", {"type": "group", "settings": {"content_direction": "row", "vertical_on_mobile": False, "gap": 12,
                                                    "width": "fit-content", "width_mobile": "fit-content", "inherit_color_scheme": True},
                     **ordered([("btn_shop", button("Shop bestsellers", "shopify://collections/all")),
                                ("btn_coll", button("Bekijk collecties", "/collections", "button-secondary"))])}),
    ]), "settings": {
        # Productfoto's van de mascara en foundation naast elkaar; op mobiel alleen de mascara
        "media_type_1": "image", "image_1": "shopify://shop_images/WhatsApp_Image_2026-07-02_at_07.58.57.jpg",
        "media_type_2": "image", "image_2": "shopify://shop_images/shopify_product_1600x2000_35fe795d-3c83-452e-8a76-723e0a9a2716.png",
        "custom_mobile_media": True, "media_type_1_mobile": "image",
        "image_1_mobile": "shopify://shop_images/WhatsApp_Image_2026-07-02_at_07.58.57.jpg",
        "content_direction": "column", "vertical_on_mobile": True,
        "horizontal_alignment_flex_direction_column": "center",
        "vertical_alignment_flex_direction_column": "center", "gap": 20,
        "section_width": "full-width", "section_height": "custom", "section_height_custom": 80,
        "color_scheme": "scheme-6", "toggle_overlay": True, "overlay_color": "#00000066",
        "overlay_style": "gradient", "gradient_direction": "to top",
        "padding-block-start": 64, "padding-block-end": 64}},

    "trust": {"type": "_blocks", "name": "Voordelen", **ordered([
        ("usp", {"type": "ai_gen_block_1e9e953", "settings": {
            "desktop_width_percent": 100, "background_color": CREAM,
            "padding_top": 28, "padding_bottom": 28, "padding_horizontal": 16,
            "padding_top_mobile": 20, "padding_bottom_mobile": 20, "padding_horizontal_mobile": 12,
            "section_spacing": 20, "show_payment_icons": True,
            "payment_bg_color": WHITE, "payment_border_color": "#ddd2c3", "payment_border_radius": 0,
            "columns_desktop": "3", "columns_mobile": "3",
            "show_feature_1": True, "feature_1_title": "Gratis verzending", "feature_1_text": "Op elke bestelling",
            "show_feature_2": True, "feature_2_title": "Veilig betalen", "feature_2_text": "iDEAL · Klarna",
            "show_feature_3": True, "feature_3_title": "Persoonlijke service", "feature_3_text": "Ma–vr 09:00–17:00",
            "icon_size": 28, "icon_color": ROSE, "title_font_weight": "500",
            "title_color": COCOA, "text_color": COCOA_TEXT}, "blocks": {}})]),
        "settings": {**sec_flex, "color_scheme": "scheme-1", "padding-block-start": 0, "padding-block-end": 0}},

    "bestsellers": {"type": "_blocks", "name": "Bestsellers", **ordered([
        ("list", {"type": "ai_gen_block_c52cb49", "settings": {
            "collection": "",
            "selected_products": ["lashlift-waterproof-mascara", "zelfkleurende-foundation-spf15",
                                  "self-tanner-tanning-lotion", "lovaire-hairboost-shampoo",
                                  "elektrische-spray-massage-borstel-lovaire", "lovaire-support-bh"],
            "heading": "Onze bestsellers", "link_label": "Bekijk alles",
            "desktop_width_percent": 100, "heading_size": 34, "image_radius": 0,
            "background_color": CREAM, "heading_color": COCOA, "text_color": COCOA,
            "link_color": ROSE, "badge_color": ROSE, "compare_color": "#6f6f6f",
            "placeholder_color": NUDE}, "blocks": {}})]),
        "settings": {**sec_flex, "color_scheme": "scheme-1", "padding-block-start": 56, "padding-block-end": 24}},

    "collections": {"type": "collection-list", "name": "Shop per categorie", "block_order": ["title"], "blocks": {
        "title": {"type": "group", "settings": {"content_direction": "column", "gap": 8,
                                                "horizontal_alignment_flex_direction_column": "center",
                                                "width": "fill", "width_mobile": "fill", "inherit_color_scheme": True},
                  **ordered([("h", text("<h2>Shop per categorie</h2>", preset="h2", align="center", width="100%",
                                        font="var(--font-heading--family)", color="var(--color-foreground-heading)"))])},
        "static-collection-card": {"type": "_collection-card", "static": True, "settings": {
            "placement": "below_image", "horizontal_alignment": "center", "vertical_alignment": "flex-end",
            "collection_card_gap": 12, "inherit_color_scheme": True, "border": "none", "border_radius": 0},
            "blocks": {
                "collection-card-image": {"type": "_collection-card-image", "static": True, "settings": {
                    "image_ratio": "portrait", "border": "none", "border_radius": 0}, "blocks": {}},
                "ctitle": {"type": "collection-title", "settings": {
                    "alignment": "center", "type_preset": "h4", "color": "var(--color-foreground-heading)"}, "blocks": {}}},
            "block_order": ["ctitle"]}},
        "settings": {"collection_list": ["make-up", "huid-producten", "haarverzorging", "beauty-tools", "shapewear"],
                     "layout_type": "grid", "carousel_on_mobile": True, "columns": 5, "mobile_columns": "2",
                     "mobile_card_size": "60cqw", "columns_gap": 16, "rows_gap": 16, "max_collections": 5,
                     "icons_style": "arrow", "icons_shape": "none", "section_width": "page-width", "gap": 24,
                     "color_scheme": "scheme-1", "padding-block-start": 48, "padding-block-end": 56}},

    "story": {"type": "section", "name": "Over Lovaire", **ordered([
        ("eyebrow", text("<p>OVER LOVAIRE</p>", preset="h6", align="center")),
        ("heading", text("<h2>Stijl, selfcare en trendy must-haves</h2>", preset="h2", align="center",
                         max_width="narrow", font="var(--font-heading--family)", color="var(--color-foreground-heading)")),
        ("body", text("<p>Zie jij ook steeds die virale producten voorbijkomen op TikTok en Instagram? Bij Lovaire brengen we ze samen: beauty essentials die écht werken, zorgvuldig voor jou geselecteerd.</p>",
                      align="center", max_width="narrow")),
        ("cta", button("Lees ons verhaal", "shopify://pages/over-ons", "button-secondary")),
    ]), "settings": {**sec_flex, "gap": 20, "color_scheme": "scheme-4",
                     "padding-block-start": 80, "padding-block-end": 80}},

    "reviews": {"type": "ss-testimonials-2", "name": "Reviews", "blocks": {
        "r1": {"type": "testimonial", "settings": {"stars_count": 5, "text": "<p>Top ervaring met Lovaire Beauty! Mooie producten, snelle verzending en alles kwam netjes binnen. De kwaliteit is beter dan verwacht en ik bestel hier zeker vaker. Aanrader! ✨</p>", "image": "shopify://shop_images/WhatsApp_Image_2026-06-05_at_20.43.21.jpg", "author": "Laura", "job_title": "Amsterdam"}},
        "r2": {"type": "testimonial", "settings": {"stars_count": 4.5, "text": "<p>Erg tevreden met Lovaire! Mooie producten, goede kwaliteit en alles kwam netjes binnen. De website is overzichtelijk en bestellen gaat heel eenvoudig. Zeker een webshop waar ik in de toekomst vaker zal bestellen!</p>", "image": "shopify://shop_images/WhatsApp_Image_2026-06-05_at_20.50.15.jpg", "author": "Yvonne", "job_title": "Eindhoven"}},
        "r3": {"type": "testimonial", "settings": {"stars_count": 5, "text": "<p>Super blij met mijn bestelling bij Lovaire! De website werkt fijn, de producten zijn top en alles was netjes verpakt. Ik kom hier zeker vaker terug! 💕✨</p>", "image": "shopify://shop_images/WhatsApp_Image_2026-06-05_at_20.55.26.jpg", "author": "Fleur", "job_title": "Utrecht"}},
        "r5": {"type": "testimonial", "settings": {"stars_count": 4.5, "text": "<p>Lovaire heeft echt een leuke collectie. Ik kom regelmatig terug om rond te kijken en heb tot nu toe alleen maar goede ervaringen gehad. Zeker een aanrader! ✨</p>", "image": "shopify://shop_images/WhatsApp_Image_2026-06-05_at_21.09.03.jpg", "author": "Luna", "job_title": "Maastricht"}},
        "r6": {"type": "testimonial", "settings": {"stars_count": 4.5, "text": "<p>Je merkt meteen dat Lovaire aandacht besteedt aan de hele ervaring. Niet alleen de producten, maar ook de uitstraling van de webshop voelt verzorgd en luxe aan. Alles was duidelijk en ik voelde me echt gewaardeerd als klant.</p>", "image": "shopify://shop_images/WhatsApp_Image_2026-06-05_at_21.16.05.jpg", "author": "Esther", "job_title": "Tilburg"}}},
        "block_order": ["r1", "r2", "r3", "r5", "r6"],
        "settings": {"heading": "<p>Wat klanten zeggen</p>", "heading_custom": True, "heading_font": "josefin_sans_n4",
                     "heading_size": 36, "heading_size_mobile": 28, "heading_align": "center", "heading_align_mobile": "center",
                     "slider_view": 3, "slider_view_mobile": 1.2, "slider_delay": 4,
                     "card_radius": 0, "card_shadow": False, "card_content_align": "center", "card_content_align_mobile": "center",
                     "text_custom": True, "text_font": "jost_n4", "text_size": 16, "text_size_mobile": 15,
                     "author_custom": True, "author_font": "jost_n5", "job_title_custom": True, "job_title_font": "jost_n4",
                     "stars_color": ROSE, "text_color": COCOA_TEXT, "author_color": COCOA, "job_title_color": "#6f6f6f",
                     "card_bg_color": WHITE, "dots_color": ROSE, "heading_color": COCOA, "background_color": BLUSH,
                     "padding_top": 72, "padding_bottom": 72, "content_width": 1200, "lazy": True}},

    "faq": {"type": "section", "name": "Veelgestelde vragen", **ordered([
        ("heading", text("<h2>Veelgestelde vragen</h2>", preset="h2", align="center", width="100%",
                         font="var(--font-heading--family)", color="var(--color-foreground-heading)")),
        ("acc", {"type": "accordion", "settings": {"icon": "plus", "dividers": True, "type_preset": "h5",
                                                   "inherit_color_scheme": True}, **ordered([
            faq_row("q1", "Wanneer ontvang ik mijn bestelling?", "De gemiddelde levertijd is 5 tot 12 werkdagen. Zodra je bestelling is verzonden, ontvang je een e-mail met je track & trace."),
            faq_row("q2", "Wat zijn de verzendkosten?", "Niets: bij Lovaire is verzending altijd gratis."),
            faq_row("q3", "Kan ik mijn bestelling retourneren?", "Je kunt je bestelling tot 14 dagen na ontvangst retourneren. Voor hygiënische producten, zoals cosmetica en ondergoed, gelden aparte voorwaarden. Lees alles op <a href=\"/pages/bestellingen-en-levering-1\">Ruilen en retourneren</a>."),
            faq_row("q4", "Waar worden jullie producten gemaakt?", "Onze producten worden zowel lokaal als wereldwijd geproduceerd. We selecteren onze productiepartners zorgvuldig, zodat je kwaliteit krijgt voor een eerlijke prijs."),
            faq_row("q5", "Ik heb een vraag, hoe bereik ik jullie?", "Stuur ons een bericht via de <a href=\"/pages/contact\">contactpagina</a>. We reageren op werkdagen tussen 09:00 en 17:00."),
        ])}),
    ]), "settings": {**sec_flex, "gap": 32, "color_scheme": "scheme-1",
                     "padding-block-start": 72, "padding-block-end": 72}},
}, "order": ["hero", "trust", "bestsellers", "collections", "story", "reviews", "faq"]}

header_group = {"type": "header", "name": "Header", "sections": {
    "header_announcements_pbXTDf": {"type": "header-announcements", "name": "t:names.announcement_bar",
        **ordered([
            ("a1", {"type": "_announcement", "settings": {"text": "Altijd gratis verzending", "link": "shopify://pages/bestellingen-en-levering",
                                                          "font": "var(--font-accent--family)", "font_size": "0.75rem",
                                                          "letter_spacing": "loose", "case": "uppercase"}, "blocks": {}}),
            ("a2", {"type": "_announcement", "settings": {"text": "Levering in 5–12 werkdagen met track & trace", "link": "shopify://pages/verzendbeleid",
                                                          "font": "var(--font-accent--family)", "font_size": "0.75rem",
                                                          "letter_spacing": "loose", "case": "uppercase"}, "blocks": {}}),
            ("a3", {"type": "_announcement", "settings": {"text": "Veilig betalen met iDEAL & Klarna", "link": "",
                                                          "font": "var(--font-accent--family)", "font_size": "0.75rem",
                                                          "letter_spacing": "loose", "case": "uppercase"}, "blocks": {}}),
        ]),
        "settings": {"speed": 5, "section_width": "full-width", "color_scheme": "scheme-announcement-black",
                     "divider_width": 0, "padding-block-start": 10, "padding-block-end": 10}},
    "header_section": {"type": "header", "blocks": {
        "header-logo": {"type": "_header-logo", "static": True, "settings": {"hide_logo_on_home_page": False,
                                                                             "padding-block-start": 0, "padding-block-end": 0}, "blocks": {}},
        "header-menu": {"type": "_header-menu", "static": True, "settings": {
            "menu": "main-menu", "type_font_primary_size": "var(--font-size--body-md)",
            "menu_font_style": "inverse", "type_font_primary_link": "secondary", "type_case_primary_link": "none",
            "menu_style": "featured_collections", "featured_products_aspect_ratio": "4 / 5",
            "featured_collections_aspect_ratio": "4 / 5", "image_border_radius": 0, "navigation_bar": False,
            "drawer_accordion": True, "drawer_accordion_expand_first": True, "drawer_dividers": True}, "blocks": {}}},
        "settings": {"logo_position": "center", "menu_position": "left", "menu_row": "top",
                     "customer_account_menu": "customer-account-main-menu",
                     "show_search": True, "search_position": "right", "search_row": "top",
                     "show_country": True, "country_selector_style": True, "show_language": False,
                     "localization_font": "body", "localization_font_size": "0.875rem",
                     "localization_position": "right", "localization_row": "top",
                     "section_width": "page-width", "section_height": "standard",
                     "enable_sticky_header": "always", "divider_width": 1, "divider_size": "full-width", "border_width": 1,
                     "actions_display_style": "icon", "actions_font_size": "0.875rem", "actions_font": "body",
                     "actions_text_case": "none", "color_scheme_top": "scheme-1", "color_scheme_bottom": "",
                     "color_scheme_transparent": "scheme-6", "enable_transparent_header_home": False,
                     "home_color_scheme": "default", "enable_transparent_header_product": False,
                     "product_color_scheme": "default", "enable_transparent_header_collection": False,
                     "collection_color_scheme": "default"}}},
    "order": ["header_announcements_pbXTDf", "header_section"]}

footer_group = {"type": "footer", "name": "Footer", "sections": {
    "newsletter": {"type": "section", "name": "Nieuwsbrief", **ordered([
        ("h", text("<h2>Word een Lovaire insider</h2>", preset="h2", align="center",
                   font="var(--font-heading--family)", color="var(--color-foreground-heading)")),
        ("p", text("<p>Als eerste op de hoogte van nieuwe producten, acties en beauty tips.</p>", align="center")),
        ("form", {"type": "email-signup", "settings": {"width": "custom", "custom_width": 100, "inherit_color_scheme": True,
                                                       "border_style": "all", "border_width": 1, "border_radius": 0,
                                                       "style_class": "button", "display_type": "text", "label": "Aanmelden",
                                                       "integrated_button": True}, "blocks": {}}),
    ]), "settings": {**sec_flex, "gap": 16, 
                     "color_scheme": "scheme-5", "padding-block-start": 64, "padding-block-end": 64}},
    "footer": {"type": "footer", **ordered([
        ("about", text("<p><strong>Lovaire</strong></p><p>Beauty essentials die jouw natuurlijke schoonheid laten stralen.</p>", max_width="narrow")),
        ("shop", {"type": "menu", "settings": {"menu": "main-menu", "heading": "Shop", "menu_spacing": 10,
                                               "show_as_accordion": True, "accordion_icon": "plus", "inherit_color_scheme": True,
                                               "heading_preset": "h4", "link_preset": "paragraph"}, "blocks": {}}),
        ("info", {"type": "menu", "settings": {"menu": "informatie", "heading": "Informatie", "menu_spacing": 10,
                                               "show_as_accordion": True, "accordion_icon": "plus", "inherit_color_scheme": True,
                                               "heading_preset": "h4", "link_preset": "paragraph"}, "blocks": {}}),
        ("pay", {"type": "group", "settings": {"content_direction": "column", "gap": 12, "width": "fill", "width_mobile": "fill",
                                               "inherit_color_scheme": True},
                 **ordered([("h", text("<p><strong>VEILIG BETALEN</strong></p>")),
                            ("icons", {"type": "payment-icons", "settings": {"horizontal_alignment": "flex-start", "gap": 8}, "blocks": {}}),
                            ("note", text("<p>Beveiligde checkout via Shopify. Wij zien en bewaren nooit je betaalgegevens.</p>"))])}),
        ("contact", text("<p><strong>KLANTENSERVICE</strong></p><p>Ma–vr: 09:00–17:00<br/>Za: 10:00–14:00<br/>Zo: gesloten</p><p>lovairesupport@gmail.com</p><p>KVK: 42074062<br/>BTW: NL005474481B21</p>")),
    ]), "settings": {"section_width": "page-width", "gap": 40, "color_scheme": "scheme-3",
                     "padding-block-start": 56, "padding-block-end": 32}},
    "utilities": {"type": "footer-utilities", **ordered([
        ("copyright", {"type": "footer-copyright", "settings": {"show_powered_by": False, "font_size": "0.75rem", "case": "none"}, "blocks": {}}),
        ("policy_list", {"type": "footer-policy-list", "settings": {"font_size": "0.75rem", "case": "none"}, "blocks": {}}),
        ("social_icons", {"type": "social-links", "settings": {k + "_url": "" for k in ["facebook", "instagram", "youtube", "tiktok", "twitter", "threads", "linkedin", "bluesky", "snapchat", "pinterest", "tumblr", "vimeo", "custom"]}, "blocks": {}}),
    ]), "settings": {"section_width": "page-width", "gap": 24, "divider_thickness": 1,
                     "color_scheme": "scheme-3", "padding-block-start": 20, "padding-block-end": 20}}},
    "order": ["newsletter", "footer", "utilities"]}

if __name__ == "__main__":
  files = {
    "config/settings_data.json": settings_data,
    "templates/index.json": index,
    "sections/header-group.json": header_group,
    "sections/footer-group.json": footer_group,
  }
  for name, data in files.items():
    path = name.replace("/", "__")
    with open(path, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(name, len(json.dumps(data)))
