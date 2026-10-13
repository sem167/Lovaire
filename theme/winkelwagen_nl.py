"""Winkelwagenpagina duidelijk en professioneel in het Nederlands: titel, vertrouwensregel onder het totaal,
kop boven de aanbevelingen. Teksten in locales/nl.json (theme/locales__nl.json)."""
import json
TRUST = ("<p>🔒 Veilig betalen met iDEAL, Klarna en meer<br/>🚚 Altijd gratis verzending, met track &amp; trace<br/>"
         "💬 Vragen? We helpen je graag via onze <a href=\"/pages/contact\">contactpagina</a></p>")
cart = {"sections": {
  "cart-section": {"type": "main-cart", "blocks": {
    "cart-page-title": {"type": "_cart-title", "static": True, "settings": {
      "title": "Je winkelwagen", "show_count": True, "type_preset": "h2", "alignment": "left",
      "padding-block-start": 32, "padding-block-end": 0, "padding-inline-start": 0, "padding-inline-end": 0}, "blocks": {}},
    "cart-page-items": {"type": "_cart-products", "static": True, "settings": {
      "gap": 24, "image_ratio": "portrait", "dividers": True, "vendor": False,
      "padding-block-start": 0, "padding-block-end": 0, "padding-inline-start": 0, "padding-inline-end": 0}, "blocks": {}},
    "cart-page-summary": {"type": "_cart-summary", "static": True, "settings": {
      "extend_summary": True, "inherit_color_scheme": False, "color_scheme": "scheme-4", "border": "none",
      "border_width": 0, "border_opacity": 100, "border_radius": 0}, "blocks": {}},
    "trust": {"type": "text", "settings": {
      "text": TRUST, "width": "100%", "max_width": "normal", "alignment": "left", "type_preset": "rte",
      "font": "var(--font-body--family)", "color": "var(--color-foreground)", "wrap": "pretty",
      "background": True, "background_color": "#f8f1ec", "corner_radius": 12,
      "padding-block-start": 16, "padding-block-end": 16, "padding-inline-start": 18, "padding-inline-end": 18}, "blocks": {}}},
    "block_order": ["trust"],
    "settings": {"section_width": "page-width", "color_scheme": "", "padding-block-start": 0, "padding-block-end": 0}},
  "product_list_xQXFMQ": {"type": "product-list", "name": "Aanbevolen", "blocks": {
    "static-header": {"type": "_product-list-content", "static": True, "settings": {
      "content_direction": "column", "vertical_on_mobile": True, "horizontal_alignment": "flex-start", "vertical_alignment": "center",
      "align_baseline": False, "horizontal_alignment_flex_direction_column": "flex-start", "vertical_alignment_flex_direction_column": "center",
      "gap": 12, "width": "fill", "custom_width": 100, "width_mobile": "fill", "custom_width_mobile": 100, "height": "fit",
      "custom_height": 100, "inherit_color_scheme": True, "color_scheme": "", "background_media": "none", "video_position": "cover",
      "background_image_position": "cover", "border": "none", "border_width": 1, "border_opacity": 100, "border_radius": 0,
      "padding-block-start": 0, "padding-block-end": 0, "padding-inline-start": 0, "padding-inline-end": 0},
      "blocks": {"text_k9HQr4": {"type": "text", "name": "t:names.heading", "settings": {
        "text": "<h2>Maak je routine compleet</h2>", "width": "fit-content", "max_width": "normal", "alignment": "left",
        "type_preset": "h4", "font": "var(--font-body--family)", "font_size": "1rem", "line_height": "normal",
        "letter_spacing": "normal", "case": "none", "wrap": "pretty", "color": "var(--color-foreground)", "background": False,
        "background_color": "#00000026", "corner_radius": 0, "padding-block-start": 0, "padding-block-end": 0,
        "padding-inline-start": 0, "padding-inline-end": 0}, "blocks": {}}},
      "block_order": ["text_k9HQr4"]},
    "static-product-card": {"type": "_product-card", "name": "t:names.product_card", "static": True, "settings": {
      "product_card_gap": 8, "inherit_color_scheme": True, "color_scheme": "", "border": "none", "border_width": 1,
      "border_opacity": 100, "border_radius": 0, "padding-block-start": 0, "padding-block-end": 0,
      "padding-inline-start": 0, "padding-inline-end": 0},
      "blocks": {
        "product_card_gallery_x7GdeL": {"type": "_product-card-gallery", "name": "t:names.product_image", "settings": {
          "image_ratio": "portrait", "border": "none", "border_width": 1, "border_opacity": 100, "border_radius": 0,
          "padding-block-start": 0, "padding-block-end": 0, "padding-inline-start": 0, "padding-inline-end": 0}, "blocks": {}},
        "group_g4dHyz": {"type": "_product-card-group", "name": "t:names.group", "settings": {
          "open_in_new_tab": False, "content_direction": "column", "vertical_on_mobile": True, "horizontal_alignment": "flex-start",
          "vertical_alignment": "center", "align_baseline": False, "horizontal_alignment_flex_direction_column": "flex-start",
          "vertical_alignment_flex_direction_column": "center", "gap": 4, "width": "fill", "custom_width": 100,
          "width_mobile": "fill", "custom_width_mobile": 100, "height": "fit", "custom_height": 100, "inherit_color_scheme": True,
          "color_scheme": "", "background_media": "none", "video_position": "cover", "background_image_position": "cover",
          "border": "none", "border_width": 1, "border_opacity": 100, "border_radius": 0, "toggle_overlay": False,
          "overlay_color": "#00000026", "overlay_style": "solid", "gradient_direction": "to top",
          "padding-block-start": 0, "padding-block-end": 0, "padding-inline-start": 0, "padding-inline-end": 0},
          "blocks": {
            "product_title_qaTmcL": {"type": "product-title", "name": "t:names.product_title", "settings": {
              "width": "fit-content", "max_width": "normal", "alignment": "left", "type_preset": "h5",
              "font": "var(--font-body--family)", "font_size": "1rem", "line_height": "normal", "letter_spacing": "normal",
              "case": "none", "wrap": "pretty", "color": "var(--color-foreground)", "background": False,
              "background_color": "#00000026", "corner_radius": 0, "padding-block-start": 0, "padding-block-end": 0,
              "padding-inline-start": 0, "padding-inline-end": 0}, "blocks": {}},
            "price_ih43pw": {"type": "price", "name": "t:names.product_price", "settings": {
              "show_sale_price_first": True, "show_installments": False, "show_tax_info": False, "type_preset": "h6",
              "width": "100%", "alignment": "left", "font": "var(--font-body--family)", "font_size": "1rem",
              "line_height": "normal", "letter_spacing": "normal", "case": "none", "color": "var(--color-foreground)",
              "padding-block-start": 0, "padding-block-end": 0, "padding-inline-start": 0, "padding-inline-end": 0}, "blocks": {}},
            "swatches_GRxyPH": {"type": "swatches", "name": "t:names.swatches", "disabled": True, "settings": {
              "product_swatches_alignment": "flex-start", "product_swatches_alignment_mobile": "flex-start", "hide_padding": False,
              "product_swatches_padding_top": 4, "product_swatches_padding_bottom": 0, "product_swatches_padding_left": 0,
              "product_swatches_padding_right": 0}, "blocks": {}}},
          "block_order": ["product_title_qaTmcL", "price_ih43pw", "swatches_GRxyPH"]}},
      "block_order": ["product_card_gallery_x7GdeL", "group_g4dHyz"]}},
    "settings": {"collection": "all", "layout_type": "grid", "carousel_on_mobile": False, "max_products": 4, "columns": 4,
                 "mobile_columns": "2", "mobile_card_size": "60cqw", "columns_gap": 8, "rows_gap": 36, "icons_style": "none",
                 "icons_shape": "circle", "section_width": "page-width", "horizontal_alignment": "flex-start", "gap": 28,
                 "color_scheme": "scheme-1", "padding-block-start": 48, "padding-block-end": 48}}},
  "order": ["cart-section", "product_list_xQXFMQ"]}
json.dump(cart, open("templates__cart.json", "w"), ensure_ascii=False, indent=2)
nl = json.load(open("locales__nl.json"))
print(json.dumps({"themeId": "gid://shopify/OnlineStoreTheme/209095164243", "files": [
  {"filename": "locales/nl.json", "body": {"type": "TEXT", "value": json.dumps(nl, ensure_ascii=False, separators=(",", ":"))}},
  {"filename": "templates/cart.json", "body": {"type": "TEXT", "value": json.dumps(cart, ensure_ascii=False, separators=(",", ":"))}}]},
  ensure_ascii=True))
